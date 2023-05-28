from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-m)wkz06botio$68@3!88$2q=%t9@dg$0397p*nw*h9c-w1ab@^'

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


try:
    from .local import *
except ImportError:
    pass
