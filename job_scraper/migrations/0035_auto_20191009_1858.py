# Generated by Django 2.2.6 on 2019-10-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0034_new_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
    ]
