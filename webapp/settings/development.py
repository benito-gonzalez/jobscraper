from webapp.settings.common import *

DEBUG = True
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FEEDBACK_PASSWORD = ""

SECRET_KEY = 's4#vnprrw^6zbn6s0j-k7axk$hlf51^@efredv!su&d_^*v2cd'
GOOGLE_RECAPTCHA_SECRET_KEY = "6Lf8EI8UAAAAAGVdCFubNmAvRw31QV-mrCPDm0G_"
