# from django.conf import settings


SECRET_KEY = 'key'

INSTALLED_APPS = (
    'models_app',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'badim',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

def get_root(*x):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *x)