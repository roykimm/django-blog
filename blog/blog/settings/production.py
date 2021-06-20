from .base import *

DEBUG = False

ALLOWED_HOSTS = ['18.222.188.155', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'django_blog',
        'USER' : '',
        'PASSWORD': '',
        'HOST' : '18.222.188.155',
        'PORT' : '5432'
    }
}