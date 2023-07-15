from .base import *
import os
from configparser import RawConfigParser

config = RawConfigParser()
config.read('/etc/vybz/settings.ini')

DEBUG = True

SECRET_KEY = config.get('section', 'VYBZ_KEY')

ALLOWED_HOSTS = ["*"]

SECURE_SSL_REDIRECT = False

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
    from .local import *
except ImportError:
    pass
