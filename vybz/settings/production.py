from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=False
)

# Raises Django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# ADMINS = (
#     ('Chris U', 'chrisuzoewulu@gmail.com'),
# )

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['138.197.169.241',
                 'www.justvybz.com', 'justvybz.com', 'localhost']

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

config = RawConfigParser()
config.read('/etc/snmov/settings.ini')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
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
