from . base import  *

SECRET_KEY = 'django-insecure-62+orsi5)#@^a=ps8bf4xn8)fx5otsg6lk776+j@c+kuj!u*$5'

DEBUG = True

ALLOWED_HOSTS = ['localhost','103.3.60.226']

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
