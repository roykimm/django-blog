from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'django_blog',
        'USER' : 'bella',
        'PASSWORD': 'bella',
        'HOST' : '18.222.188.155',
        'PORT' : '5432'
    }
}