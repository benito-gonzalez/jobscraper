# Generated by Django 2.1.2 on 2019-08-14 18:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('job_scraper', '0030_new_companies'), ]

    operations = [migrations.RunSQL("""
            INSERT INTO "Cities"("name", "region_id") VALUES ('Levi', (select id from "Regions" where name like 'Lappi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Saariselkä', (select id from "Regions" where name like 'Lappi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Vääksy', (select id from "Regions" where name like 'Päijät-Häme'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Vihanti', (select id from "Regions" where name like 'Pohjois-Pohjanmaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Leppävesi', (select id from "Regions" where name like 'Keski-Suomi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Renko', (select id from "Regions" where name like 'Kanta-Häme'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Ruoholahti', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Piikkiö', (select id from "Regions" where name like 'Varsinais-Suomi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Suolahti', (select id from "Regions" where name like 'Keski-Suomi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Kulloo', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Nummela', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Pankakoski', (select id from "Regions" where name like 'Pohjois-Karjala'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Jalasjärvi', (select id from "Regions" where name like 'Etelä-Pohjanmaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Ivalo', (select id from "Regions" where name like 'Lappi'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Muuruvesi', (select id from "Regions" where name like 'Pohjois-Savo'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Useita paikkakuntia', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Karjaa', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Pääkaupunkiseutu', (select id from "Regions" where name like 'Uusimaa'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Hammaslahti', (select id from "Regions" where name like 'Pohjois-Karjala'));
            INSERT INTO "Cities"("name", "region_id") VALUES ('Hyvinge', (select id from "Regions" where name like 'Uusimaa'));
            """)]
