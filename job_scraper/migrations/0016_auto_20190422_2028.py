# Generated by Django 2.1.2 on 2019-04-22 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0015_clickcounter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='clickcounter',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]