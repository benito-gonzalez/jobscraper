# Generated by Django 2.1.2 on 2019-04-19 10:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0014_new_companies'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.PositiveSmallIntegerField(default=0)),
                ('apply', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_scraper.Job')),
            ],
            options={
                'db_table': 'ClickCounter',
            },
        ),
    ]
