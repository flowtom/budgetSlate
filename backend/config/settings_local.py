from .settings import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='budgetslate'),
        'USER': config('DB_USER', default='alaena'),
        'PASSWORD': config('DB_PASSWORD', default='cookie'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Add any other local-specific settings here. 