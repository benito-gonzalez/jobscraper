import os
import sys
import datetime
import codecs

from django.conf import settings
from django.core.mail import send_mail

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/secretkey.txt'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')


my_path = os.path.abspath(os.path.dirname(__file__))
SCRAPERLOG = os.path.join(my_path, "logs/scraper.log")


def main():
    now = datetime.datetime.now().strftime("%d-%m-%Y")
    try:
        error_lines = []
        with codecs.open(SCRAPERLOG, "r", encoding='utf-8', errors='ignore') as file:
            previous_line = None
            for line in file:
                if line.startswith("[" + now) and "ERROR" in line:
                    if "ERROR" not in previous_line:
                        error_lines.append(previous_line)
                    error_lines.append(line)
                previous_line = line

        if error_lines:
            send_mail(
                'Scraper errors on ' + now,
                ''.join(error_lines),
                settings.EMAIL_HOST_USER,
                ['gon.beni@gmail.com'],
                fail_silently=False,
            )

    except FileNotFoundError:
        sys.exit("Log file does not exist")


if __name__ == "__main__":
    # execute only if run as a script
    main()
