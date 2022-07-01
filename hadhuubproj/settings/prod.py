from . base import *
from decouple import config

ALLOWED_HOSTS = ['www.hadhuub.com','103.3.60.226','127.0.0.1']
# ALLOWED_HOSTS = ['localhost','103.3.60.226']

DEBUG = True

# INSTALLED_APPS +=[
#     'django.contrib.postgres',
# ]
SECRET_KEY = config('SECRET_KEY')

#For heroku Specific 
# import dj_database_url 
# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

# import django_heroku
# django_heroku.settings(locals())


# DATABASES = {
#      'default': {
#      'ENGINE': 'django.db.backends.postgresql_psycopg2',
#      'NAME': 'hadhuubdb',
#      'USER': 'hadhuubuser',
#      'PASSWORD': 'Dh!ga3eS0ft',
#      'HOST': 'localhost',
#      'PORT': '5432',
#      }
#  }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "hadhuubo@gmail.com"
EMAIL_HOST_PASSWORD = "mfdglqghmbqqmysj"


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'