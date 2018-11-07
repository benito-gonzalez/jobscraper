# Generated by Django 2.1.2 on 2018-11-07 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO 'Companies'('name', 'logo') VALUES ('DNA', 'dna.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Elisa', 'elisa.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Flashnode Oy', 'flashnode.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Vala Group Oy', 'vala_group.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Siili Solutions Oyj', 'siili.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Innofactor Oyj', 'innofactor.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Smarp Oyj', 'smarp.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Silo.AI Oy', 'silo.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('ABB Oy', 'abb.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Qvik Oy', 'qvik.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Blueprint Genetics Oy', 'blueprint.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Eficode Oy', 'eficode.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Ericsson', 'ericsson.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Varjo Technologies', 'varjo.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Telia Finland Oyj', 'telia.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Wärtsilä', 'wartsila.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Nordea', 'nordea.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Tieto', 'tieto.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Rightware', 'rightware.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Rovio', 'rovio.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Futurice', 'futurice.png');
            INSERT INTO 'Companies'('name', 'logo') VALUES ('Supercell', 'supercell.png');
            """
        ),
    ]
