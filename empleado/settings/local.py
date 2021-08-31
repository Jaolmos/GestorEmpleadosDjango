from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #Todos los datos de la base de datos POSTGRESQL
        'NAME': ('empleado_db'),
        'USER': ('josea'),
        'PASSWORD': ('djangopass'),
        'HOST': ('localhost'),
        'PORT': ('5432'),

    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

