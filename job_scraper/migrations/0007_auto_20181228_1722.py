# Generated by Django 2.1.2 on 2018-12-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0006_job_updated_at'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nokia', 'nokia.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Verto Analytics', 'verto.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Efecte Oyj', 'efect.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nets', 'nets.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Danske Bank', 'danske.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nordcloud', 'nordcloud.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nebula Oy', 'telia.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Digital goodie', 'digital.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nightingale Health', 'nightingale.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Sandvik', 'sandvik.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Signant Health', 'signant_health.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('OP Financial Group', 'op.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Dream Broker', 'dream.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Relex', 'relex.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('F-Secure', 'f-secure.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Outotec', 'outotec.png');
            """
        ),
    ]
