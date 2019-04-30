from django.db import migrations


def add_logo100(apps, schema_editor):
    company_instance = apps.get_model("job_scraper", "Company")
    for company in company_instance.objects.all():
        logo_name = company.logo
        name = logo_name.name.split(".png")[0]
        company.logo100 = name + "_100.png"
        company.save()


class Migration(migrations.Migration):

    dependencies = [
        ('job_scraper', '0019_auto_20190430_1715'),
    ]

    operations = [
        migrations.RunPython(add_logo100),
    ]
