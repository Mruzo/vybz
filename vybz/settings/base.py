
from pathlib import Path
import os
import mimetypes
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=True
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feedback',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

LOGIN_URL = '/login/'

# redirect a logged in user to the homepage
LOGIN_REDIRECT_URL = "/"

# how would users sign in? username and email
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# as soon as user clicks link in their email, the account is confirmed
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# redirect to the login url after email confirmation
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL

# email sign up requried
ACCOUNT_EMAIL_REQUIRED = True

# always verify email
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# login once email confirmed
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# no need to fill a form to logout
ACCOUNT_LOGOUT_ON_GET = True

# login once password is reset
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# redirect to the login page after logging out
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_URL

# username in any casing as long as it is spelt dback/feedback/1/change/
ACCOUNT_SESSION_REMEMBER = True

# forbidden usernamespython manage.py makemigrations
ACCOUNT_USERNAME_BLACKLIST = ["justvybz", "vybz",
                              "misteruzo", "badbele", "uzo", "admin", "god"]

# mininum length of username
ACCOUNT_USERNAME_MIN_LENGTH = 3


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vybz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, "vybz/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vybz.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)
