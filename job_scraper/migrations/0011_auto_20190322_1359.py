# Generated by Django 2.1.2 on 2019-03-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0010_renamed_logos'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTagMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_times', models.PositiveSmallIntegerField(default=0)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_scraper.Job')),
            ],
            options={
                'db_table': 'JobsTagsMap',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='jobtagmap',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_scraper.Tag'),
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(through='job_scraper.JobTagMap', to='job_scraper.Tag'),
        ),
    ]
