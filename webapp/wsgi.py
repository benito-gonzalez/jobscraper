"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(__file__)
if os.path.isfile(BASE_DIR + '../../.keys/secretkey.txt'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')

application = get_wsgi_application()
