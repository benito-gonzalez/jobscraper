import os
import django
import csv
from job_scraper.utils import db_support

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../../webapp/.is_development'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')

django.setup()

my_path = os.path.abspath(os.path.dirname(__file__))
FILENAME = os.path.join(my_path, "keywords.csv")


def read_keywords_csv():
    keywords = []

    with open(FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            keywords.append(", ".join(row))

    return keywords


def main():
    keywords = read_keywords_csv()
    for keyword in keywords:
        db_support.add_keyword(keyword)


if __name__ == "__main__":
    # execute only if run as a script
    main()
