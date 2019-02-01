# Generated by Django 2.1.2 on 2019-01-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0007_auto_20181228_1722'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Kone', 'kone.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Smartly.io', 'smartly.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Cybercom Finland Oy', 'cybercom.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Enfo Oyj', 'enfo.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Sofigate', 'sofigate.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('MPY', 'mpy.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Blue Meteorite', 'blue_meteorite.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Sulava', 'sulava.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nitor', 'nitor.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Softability', 'softability.png');
            """
        )
    ]