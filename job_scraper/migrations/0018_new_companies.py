# Generated by Django 2.1.2 on 2019-04-24 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0017_usersearches'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Autori Oy', 'autori.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('720 Degrees Oy', '720_degrees.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Umbra', 'umbra.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Lumoame Oy', 'lumoame.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Screenful Oy', 'screenful.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Teleste Corporation', 'teleste.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Sujuwa Group', 'sujuwa_group.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Vaana', 'vaana.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('IWA', 'iwa.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nico', 'nice_business_consulting.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Bitwise', 'bitwise.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Solteq', 'solteq.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('University of Turku', 'university_of_turku.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('University of Helsinki', 'university_of_helsinki.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('University of Jyväskylä', 'university_of_jyvaskyla.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Aalto University', 'aalto_university.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Tampere University', 'tampere_university.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('University of Oulu', 'university_of_oulu.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Alphasense', 'alpha_sense.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Visma', 'visma.png');
            """
        )
        ]