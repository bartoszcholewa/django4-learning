from .base import *

SECRET_KEY = 'django-insecure-inbpxf)4shpglb0+w5h#p*r6*@+k*j%bf+#x*#-_vmmp243p4q'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 0
EMAIL_USE_TLS = True
