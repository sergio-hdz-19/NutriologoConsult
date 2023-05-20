from .base import *
import environ

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env()
# reading .env file
environ.Env.read_env()


DEBUG = True

ALLOWED_HOSTS = []




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_ADDON_DB'),
        'USER': env('POSTGRESQL_ADDON_USER'),
        'PASSWORD': env('POSTGRESQL_ADDON_PASSWORD'),
        'HOST': env('POSTGRESQL_ADDON_HOST'),
        'PORT': env('POSTGRESQL_ADDON_PORT'),
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/




STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
