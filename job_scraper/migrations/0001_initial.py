# Generated by Django 2.1.2 on 2018-11-01 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=5000)),
                ('location', models.CharField(max_length=100)),
                ('salary', models.FloatField(blank=True, default=None, null=True)),
                ('pub_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('job_type', models.CharField(max_length=500)),
                ('highlighted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_scraper.Company')),
            ],
            options={
                'db_table': 'Jobs',
            },
        ),
    ]
