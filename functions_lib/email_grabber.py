import imaplib
import email
from email.header import decode_header
import datetime as dt
import json


def get_emails(username, password, server_config, current_date):
    imap = imaplib.IMAP4_SSL(server_config)
    imap.login(username, password)

    formated_date = current_date.strftime('%d-%b-%Y')

    status, messages = imap.select("INBOX")

    email_list = imap.search(None, f'ON "{formated_date}"')[1]
    email_list = email_list[0].split()
    message_list = []
    for email_byte in email_list:
        # fetch the email message by ID
        res, msg = imap.fetch(email_byte, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding)
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes) and encoding is not None:
                    From = From.decode(encoding)
                message_tuple = (From, subject, msg)
                message_list.append(message_tuple)

    imap.close()
    imap.logout()

    return message_list


def get_credentials():
    json_file = open('config_files/login.json', 'r')
    credentials = json.load(json_file)
    json_file.close()

    return credentials
