from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*!y0$9i(y%f5^&c!s!2d16wl*d3uf-xbl@8+kv47eo)79ect)v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grocerystore',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'pass123'
    }
}
