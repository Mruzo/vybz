from .base import *
import os
from configparser import RawConfigParser

config = RawConfigParser()
config.read('/etc/vybz/settings.ini')


# Raises Django's ImproperlyConfigured exception if SECRET_KEY not in os.environ


# ADMINS = (
#     ('Chris U', 'chrisuzoewulu@gmail.com'),
# )

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


DEBUG = False

ALLOWED_HOSTS = ['138.197.169.241',
                 'www.justvybz.com', 'justvybz.com', 'localhost']

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

config = RawConfigParser()
config.read('/etc/snmov/settings.ini')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config.get('section', 'DB_NAME'),
        'USER': config.get('section', 'DB_USER'),
        'PASSWORD': config.get('section', 'DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

AWS_ACCESS_KEY_ID = env('S3_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('S3_SCRT_KEY')
AWS_STORAGE_BUCKET_NAME = env('S3_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'snm.storage_backends.MediaStorage'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


try:
    from .local import *
except ImportError:
    pass
