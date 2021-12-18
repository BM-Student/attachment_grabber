import email
import datetime as dt
import os
import json


def read_emails(email_list, check_datetime):
    path_mapping = get_mapping_file()
    grabbed_files = []
    for From, subject, msg in email_list:
    # for From, subject, msg in email_list:
        # datetime_received = read_date_tup(msg['Date'])
        # if date_check(datetime_received, datetime_received) is False:
        #    continue
        body_container = []
        if msg.is_multipart():
            # iterate over email parts
            for part in msg.walk():
                # extract content type of email
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                try:
                    # get the email body
                    body = part.get_payload(decode=True).decode()
                    body_container.append(body)
                except:
                    body = part.get_payload()
                if "attachment" in content_disposition:
                    if len(body_container) != 0:
                        body = body_container[0]
                    # download attachment
                    filename = part.get_filename()
                    if filename:
                        filename = repr(filename)
                        filename = filename.replace('\r', '').replace('\n', '').replace('\\', '').replace("'", "")
                        # download attachment and save it
                        folder = apply_mapping_file(
                            path_mapping, check_datetime, From=From, subject=subject
                        )
                        print(folder)
                        if isinstance(folder, str) is False:
                            continue
                        try:
                            if filename in os.listdir(folder):
                                print('already Grabbed')
                            else:
                                #print(f'Grabbing File: {filename}')
                                grabbed_files.append(filename)
                                open(f'{folder}/{filename}', "wb").write(part.get_payload(decode=True))

                        except FileNotFoundError:
                            f = open(f'{folder}/errors_{dt.datetime.now().date()}.txt', 'a')
                            f.write(f'{"="*50}\n')
                            f.write(f'{From}|{subject}|{filename}\n')
                            f.write(f'{"=" * 50}\n')
                            f.close()
    if len(grabbed_files) == 0:
        print('No Files Grabbed')
    else:
        print('Grabbed the following file(s):')
        for f in grabbed_files:
            print(f'\t{f}')
    return grabbed_files


def get_mapping_file():
    json_file = open('config_files/path_mapping.json', 'r')
    path_mapping = json.load(json_file)
    json_file.close()

    return path_mapping


def apply_mapping_file(path_mapping, check_datetime, **email_ats):
    for path, check in path_mapping.items():
        if ',' in path:
            path_flags = list(path.split(' |Flags: ')[-1])
        else:
            path_flags = [path.split(' |Flags: ')[-1]]
        print(path_flags)
        path = apply_flags(path.split(' |Flags: ')[0], path_flags, check_datetime)
        count = 0
        for key, val in email_ats.items():
            if len(check[key]) == 0 or check[key] in str(val):
                count += 1
        if count == len(list(email_ats.items())):
            return path


def apply_flags(path, flags, check_datetime):
    if 'di' in flags:
        path = f'{path}/{check_datetime.date() - dt.timedelta(days=check_datetime.weekday())}'
        if os.path.isdir(path) is False:
            os.mkdir(path)

    return path


def error_handling():
    pass


def read_date_tup(date_tup):
    if ',' in date_tup:
        date_tup = ' '.join(date_tup.split(' ')[1:])
    if '(' in date_tup:
        date_tup = ' '.join(date_tup.split(' ')[:-1])
    off_set_to_est = (-500 - int(date_tup.split(' ')[-1]))/100
    print(off_set_to_est)
    if len(str(date_tup.split(' ')[0])) < 2:
        date_tup = f'0{date_tup}'
    datetime_return = dt.datetime.strptime(' '.join(date_tup.split(' ')[:-1]),
                                           '%d %b %Y %H:%M:%S') + dt.timedelta(hours=off_set_to_est)

    return datetime_return


def date_check(datetime_received, check_datetime):
    date_tup_mins = datetime_received.hour * 60 + datetime_received.minute
    check_datetime_mins = check_datetime.hour * 60 + check_datetime.minute

    if date_tup_mins >= check_datetime_mins:
        return True
    else:
        return False
