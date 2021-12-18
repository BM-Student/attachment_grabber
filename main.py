import functions_lib.email_grabber as eg
import functions_lib.email_processer as ep
import datetime as dt


def main():
    check_datetime = dt.datetime(month=12, day=9, year=2021, hour=19) - dt.timedelta(minutes=5)
    credentials = eg.get_credentials()
    top_n_emails = eg.get_emails(credentials['user'], credentials['pass'], credentials['server_config'], check_datetime)
    grabbed_emails = ep.read_emails(top_n_emails, check_datetime)


if __name__ == '__main__':
    main()
