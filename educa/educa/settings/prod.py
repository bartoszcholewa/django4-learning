import os

from .base import *

SECRET_KEY = '_&kwh^odyr=lt$xr*dpejzid%apc&yz06tg&rm-=jv+*9n)ozh'
DEBUG = False
ALLOWED_HOSTS = ['.educaproject.com']


ADMINS = [
    ('Bartosz Cholewa', 'bbcholewa@gmail.com'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
# Use a secure cookie for cross-site request forgery (CSRF) protection.
# With True , browsers will only transfer the cookie over HTTPS.
CSRF_COOKIE_SECURE = True

# Use a secure session cookie. With True , browsers will only transfer
# the cookie over HTTPS.
SESSION_COOKIE_SECURE = True

# Whether HTTP requests have to be redirected to HTTPS.
SECURE_SSL_REDIRECT = True


# Email
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 0
EMAIL_USE_TLS = True
