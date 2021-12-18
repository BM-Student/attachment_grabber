import tkinter as tk
from gui_functions.remove_from_JSON import main as sub_json
import gui_functions.misc_funcs as msc_f


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.x = 750
        self.y = 600
        self.colors = {
            'light': '#F5F7FA',
            'mid': '#323F4B',
            'dark': '#1F2933',
            'highlight': '#04293A'
        }

        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.server = tk.StringVar()

        self.path = tk.StringVar()
        self.sender = tk.StringVar()
        self.subject = tk.StringVar()
        self.flags = tk.StringVar()

        self.email_cleared = self.password_cleared = self.sender_cleared = self.subject_cleared = False

        self.title_font = ('Times', 28)
        self.text_font = ('Times', 16)
        self.tab_width = int((self.x/5 - 20)/10)
        self.tab_height = int((self.y/10 - 20)/15)
        self.right_frame = tk.Frame(self.window, bg=self.colors['dark'], height=self.y - 20,
                                    width=(self.x * (4/5)) - 10)
        self.window_rules()
        self.load_data()

    def window_rules(self):
        self.window.title('Attachment Grabber Config')
        self.window.geometry(f'{self.x}x{self.y}')
        self.window.resizable(width=False, height=False)
        self.window.config(bg=self.colors['dark'])

    def load_data(self):
        self.left_hand_toggle()
        self.right_hand_interface_load('Configure')

    def left_hand_toggle(self):
        self.left_frame = tk.Frame(self.window, bg=self.colors['mid'], height=self.y - 20,
                                   width=(self.x * (1/5)) - 10)
        self.left_frame.grid_propagate(False)
        self.config_tab = tk.Button(master=self.left_frame, font=self.text_font, text='Add Rule/\nConfig', width=self.tab_width,
                                    height=self.tab_height, bg=self.colors['highlight'], fg=self.colors['dark'],
                                    activeforeground=self.colors['highlight'],
                                    activebackground=self.colors['dark'])
        self.remove_tab = tk.Button(master=self.left_frame, font=self.text_font, text='Manage\nRules',
                                    width=self.tab_width,
                                    height=self.tab_height, bg=self.colors['highlight'], fg=self.colors['dark'],
                                    activeforeground=self.colors['highlight'],
                                    activebackground=self.colors['dark'])
        self.tab_label = tk.Label(master=self.left_frame, font=self.title_font, text='TABS',
                                  width=int(self.tab_width*(3/5)), height=self.tab_height, bg=self.colors['mid'],
                                  fg=self.colors['light'])
        self.underline_left = tk.Frame(self.left_frame, bg=self.colors['light'], height=5, width=(self.x * (1/5)) - 28)

        self.left_frame.grid(column=0, row=0, padx=10, pady=10, sticky='nw')
        self.tab_label.place(relx=0.5, rely=0.08, anchor='center')
        self.underline_left.place(relx=0.5, rely=0.12, anchor='center')
        self.config_tab.place(relx=0.5, rely=0.18, anchor='center')
        self.remove_tab.place(relx=0.5, rely=0.28, anchor='center')

    def right_hand_interface_load(self, display):
        self.right_frame.grid(column=1, row=0, sticky='nw')
        if display == 'Configure':
            self.right_hand_config()
            self.right_hand_header('Configure')

    def right_hand_header(self, title):
        self.right_frame_head = tk.Frame(self.right_frame, bg=self.colors['mid'], height=int((self.y - 10)*(1/4)),
                                    width=(self.x * (4/5)) - 20)
        self.config_label = tk.Label(self.right_frame_head, bg=self.colors['mid'], text=title,
                                     fg=self.colors['light'], font=self.title_font)
        self.underline_right = tk.Frame(self.right_frame_head, bg=self.colors['light'], height=5,
                                        width=(self.x * (5/7)) - 20)
        self.overline_right = tk.Frame(self.right_frame_head, bg=self.colors['light'], height=5,
                                        width=(self.x * (5 / 7)) - 20)

        self.email_config_frame = tk.Frame(self.right_frame_head, bg=self.colors['mid'])

        self.right_frame_head.grid(column=1, row=0, padx=0, pady=10)
        self.overline_right.place(relx=0.5, rely=0.2, anchor='center')
        self.config_label.place(relx=0.5, rely=0.5, anchor='center')
        self.underline_right.place(relx=0.5, rely=0.8, anchor='center')

    def right_hand_config(self):
        self.right_frame_disp = tk.Frame(self.right_frame, bg=self.colors['mid'], height=int((self.y - 35)*(3/4)),
                                    width=(self.x * (4/5)) - 20)
        self.right_frame_disp.grid(column=1, row=1, padx=0, pady=0)

        self.email_entry = tk.Entry(self.right_frame_disp, textvariable=self.email, fg=self.colors['dark'],
                                    width=int(self.x * (1/13)))
        self.email_entry.insert(0, 'Email Address')
        self.password_entry = tk.Entry(self.right_frame_disp, textvariable=self.password, fg=self.colors['dark'],
                                       width=int(self.x * (1 / 13)), show='*')
        self.password_entry.insert(0, 'Password')

        self.submit_email = tk.Button(self.right_frame_disp, bg=self.colors['highlight'], fg=self.colors['dark'],
                                      activebackground=self.colors['dark'],
                                      activeforeground=self.colors['highlight'],
                                      text='Configure Email', font=self.text_font,
                                      command=lambda: msc_f.replace_email_config(email=self.email.get(),
                                                                                 password=self.password.get()))
        self.div_line = tk.Frame(self.right_frame_disp, bg=self.colors['dark'], height=7,
                                 width=(self.x * (7/7)))

        self.directory_select_frame = tk.Frame(self.right_frame_disp, bg=self.colors['mid'])
        self.directory_display = tk.Entry(self.directory_select_frame, bg=self.colors['light'],
                                          fg=self.colors['dark'], textvariable=self.path,
                                          width=int(self.x * (1/16))+1, state='disabled')
        self.directory_button = tk.Button(self.directory_select_frame, bg=self.colors['light'],
                                          fg=self.colors['dark'], text='Select Path',
                                          command=lambda: msc_f.select_directory(self.path))

        self.from_entry = tk.Entry(self.right_frame_disp, bg=self.colors['light'],
                                   fg=self.colors['dark'], textvariable=self.sender,
                                   width=int(self.x * (1 / 13)))
        self.from_entry.insert(0, 'Sender (full address or portion after @)')
        self.subject_entry = tk.Entry(self.right_frame_disp, bg=self.colors['light'],
                                      fg=self.colors['dark'], textvariable=self.subject,
                                      width=int(self.x * (1 / 13)))
        self.subject_entry.insert(0, 'Phrase Found in Subject')

        self.flag_holder = tk.Frame(self.right_frame_disp, bg=self.colors['mid'])
        self.time_inc_flag = tk.Radiobutton(self.flag_holder, text='Time Inc. On', fg=self.colors['light'],
                                            bg=self.colors['mid'], activebackground=self.colors['dark'],
                                            anchor='w', variable=self.flags, value='di')
        self.no_time_inc_flag = tk.Radiobutton(self.flag_holder, text='Time Inc. Off', fg=self.colors['light'],
                                            bg=self.colors['mid'], activebackground=self.colors['dark'],
                                            anchor='w', variable=self.flags, value='')
        self.add_rule_button = tk.Button(self.right_frame_disp, bg=self.colors['light'], fg=self.colors['dark'],
                                         activebackground=self.colors['dark'], activeforeground=self.colors['light'],
                                         text='Add Rule',
                                         command=lambda: msc_f.add_rule(path=self.path.get(), flags=self.flags.get(),
                                                                        sender=self.sender.get(),
                                                                        subject=self.subject.get()),
                                         font=self.text_font)

        self.directory_display.grid(row=0, column=0, padx=5)
        self.directory_button.grid(row=0, column=1, padx=5)
        self.time_inc_flag.grid(row=0, column=0, sticky='nw')
        self.no_time_inc_flag.grid(row=0, column=1, sticky='nw')

        self.email_entry.place(relx=0.5, rely=0.1, anchor='center')
        self.password_entry.place(relx=0.5, rely=0.2, anchor='center')
        self.submit_email.place(relx=0.5, rely=0.3, anchor='center')
        self.div_line.place(relx=0.5, rely=0.37, anchor='center')
        self.directory_select_frame.place(relx=0.5, rely=0.49, anchor='center')
        self.from_entry.place(relx=0.5, rely=0.59, anchor='center')
        self.subject_entry.place(relx=0.5, rely=0.68, anchor='center')
        self.flag_holder.place(relx=0.5, rely=0.75, anchor='center')
        self.add_rule_button.place(relx=0.5, rely=0.85, anchor='center')


if __name__ == '__main__':
    window = Main()
    window.window.mainloop()
    # add_json('config_files/path_mapping.json', {'Test |Flags: ': {'one': '1', 'two': '2'}})
    # sub_json('config_files/path_mapping.json', 'Test')
