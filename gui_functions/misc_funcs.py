from tkinter import messagebox
from tkinter import filedialog
from gui_functions.add_to_JSON import main as add_json
import json


def clear_default(clear_var, fg, cleared):
    if cleared is False:
        clear_var.delete(0, -1)
        clear_var.config(fg=fg)

    return True


def replace_email_config(email, password, server='outlook.office365.com'):
    if '@' not in email:
        messagebox.showerror('Invalid Email', '@ not present in email address')
    else:
        json_f = open('config_files/login.json', 'w')
        dict_ob = {
            'user': email,
            'pass': password,
            'server_config': server
        }
        json.dump(dict_ob, json_f, indent=4)
        json_f.close()
        messagebox.showinfo('Email Updated', 'Email Configuration Data Updated')


def select_directory(path_var):
    filename = filedialog.askdirectory()
    path_var.set(filename)


def add_rule(path, flags, subject, sender):
    add_json('config_files/path_mapping.json',
             {f'{path} |Flags: {flags}': {'subject': subject, 'From': sender}})
    messagebox.showinfo('Rule Added', f'New Rule Added\n\t-From: {sender}\n\t-Subject: {subject}')
