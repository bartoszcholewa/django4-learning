# Copy me to new file settings_local.py and update my variables

SECRET_KEY = 'change-me'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Email
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_HOST_USER = 'change-me'
EMAIL_HOST_PASSWORD = 'change-me'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Stripe settings
STRIPE_PUBLISHABLE_KEY = 'change-me'
STRIPE_SECRET_KEY = 'change-me'
STRIPE_WEBHOOK_SECRET = 'change-me'
STRIPE_API_VERSION = '2022-11-15'
