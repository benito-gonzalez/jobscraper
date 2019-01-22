from webapp.settings.common import *

ALLOWED_HOSTS = ['91.217.83.113']

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Use a separate file for the secret key
with open(os.path.join(BASE_DIR, 'secretkey.txt')) as f:
    SECRET_KEY = f.read().strip()


# Production configs
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_PRELOAD = True

with open(os.path.join(BASE_DIR, 'email_pwd.txt')) as f:
    EMAIL_HOST_PASSWORD = f.read().strip()
