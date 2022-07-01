from . base import *
from decouple import config

ALLOWED_HOSTS = ['localhost','103.3.60.226']

DEBUG = False

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
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'hadhuubdb',
#     'USER': 'hadhuubuser',
#     'PASSWORD': 'Dhigane)(*&^',
#     'HOST': 'localhost',
#     'PORT': '',
#     }
# }

DATABASES = {
     'default': {
     'ENGINE': 'django.db.backends.postgresql_psycopg2',
     'NAME': 'hadhuubdb',
     'USER': 'hadhuubuser',
     'PASSWORD': 'Dh!ga3eS0ft',
     'HOST': 'localhost',
     'PORT': '5432',
     }
 }
