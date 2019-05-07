from .settings_base import *


DATABASES['default'].update(
    {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
)

STATIC_ROOT = '/static'

DEBUG = True

ALLOWED_HOSTS.append('backend')

SITE_ID = 3