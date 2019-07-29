# Generated by Django 2.1.2 on 2019-07-23 13:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('job_scraper', '0025_new_companies'), ]

    operations = [migrations.RunSQL("""
            INSERT INTO 'Companies'('name', 'logo', 'logo100', 'description') VALUES ('Vainu.io', 'vainu.png', 'vainu_100.png', '<p>At Vainu we''re currently on a mission to collect, read and understand all the information ever written about every company in the world, and then make this information comprehensible to everyone.</p><p>Founded in Helsinki in 2014, we revolutionise how companies use big data in order to sell more.</p>');
            INSERT INTO 'Companies'('name', 'logo', 'logo100', 'description') VALUES ('Dear Lucy', 'dear_lucy.png', 'dear_lucy_100.png', '<p>Dear Lucy is a privately owned scale-up software company founded in 2014. Our customers are companies and public sector organizations that value data-driven management and where transparency is at the heart of organizational culture.</p><p>Our mission is to make companies smarter. We help teams and organisations make better decisions and react faster by making core business data available easily and effortlessly.</p>');
            INSERT INTO 'Companies'('name', 'logo', 'logo100', 'description') VALUES ('Electronic Arts', 'ea.png', 'ea_100.png', '<p>Electronic Arts Inc. is a global leader in digital interactive entertainment.</p><p>EA develops and delivers games, content and online services for Internet-connected consoles, mobile devices and personal computers.</p>');
            INSERT INTO 'Companies'('name', 'logo', 'logo100', 'description') VALUES ('Sniffie', 'sniffie.png', 'sniffie_100.png', '<p>We believe easy price monitoring should be the norm in any business. Complex, tedious software makes people cranky. We are here to change this with Sniffie.</p><p>It is not either wise or nice to buy excessive amounts of data and start analysing it, if the only thing you need to monitor is your local competition.</p>');
            INSERT INTO 'Companies'('name', 'logo', 'logo100', 'description') VALUES ('Wolt', 'wolt.png', 'wolt_100.png', '<p>Wolt is a technology company building the one app for food. Be it discovering or getting great meals – takeaway, home delivery or to the table – Wolt takes care of it for you. Pick a restaurant, build your order, choose delivery, takeaway or eat in and hit send. Magic ensues.</p><p>Our headquarter is in Helsinki, Finland, but we have offices in over 15 countries where people enjoy the magic of Wolt.</p>');
        """)]
