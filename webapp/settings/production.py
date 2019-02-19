from webapp.settings.common import *

ALLOWED_HOSTS = ['91.217.83.113', 'www.jobsportal.fi', 'jobsportal.fi']

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Use a separate file for the secret key
with open(os.path.join(BASE_DIR, '../../.keys/secretkey.txt')) as f:
    SECRET_KEY = f.read().strip()

# Use a separate file for the secret key
with open(os.path.join(BASE_DIR, '../../.keys/recaptcha_secretkey.txt')) as f:
    GOOGLE_RECAPTCHA_SECRET_KEY = f.read().strip()

# Production configs
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

PREPEND_WWW = True

with open(os.path.join(BASE_DIR, '../../.keys/email_pwd.txt')) as f:
    EMAIL_HOST_PASSWORD = f.read().strip()

with open(os.path.join(BASE_DIR, '../../.keys/email_feedback_pwd.txt')) as f:
    EMAIL_FEEDBACK_PASSWORD = f.read().strip()
