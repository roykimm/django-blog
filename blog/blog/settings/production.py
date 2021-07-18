from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

DB_USER = get_secret("DB_USER")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_ENGINE = get_secret("DB_ENGINE")
DB_NAME = get_secret("DB_NAME")
DB_HOST = get_secret("DB_HOST")
DB_PORT = get_secret("DB_PORT")

DATABASES = {
    'default': {
        'ENGINE' : DB_ENGINE,
        'NAME' : DB_NAME,
        'USER' : DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST' : DB_HOST,
        'PORT' : DB_PORT
    }
}