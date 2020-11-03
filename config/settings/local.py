from .common import *  # noqa
from .common import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='VcGUXxAe0nZsSUHOo4r3muwhOwLEAqX5hCiaXADhBKL1wmsn9umZHjeMne9cVdjl',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:////{}/local.sqlite3'.format(ROOT_DIR))
}

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# Before enabling email, install mailhog--or your preferred SMTP testing service.
# https://github.com/mailhog/MailHog

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = env(
#     'DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend'
# )
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
# EMAIL_TIMEOUT = 5

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = 'localhost'

# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = 1025
