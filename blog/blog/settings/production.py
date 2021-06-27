from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'django_blog',
        'USER' : 'bella',
        'PASSWORD': 'bella',
        'HOST' : 'gobella.kr',
        'PORT' : '5432'
    }
}