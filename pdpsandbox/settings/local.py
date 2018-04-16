from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdpsandbox',
    }
}

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += [
    'django_extensions'
]
