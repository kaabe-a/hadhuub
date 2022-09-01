from . base import *
from decouple import config

# ALLOWED_HOSTS = ['127.0.0.1','localhost']
# ALLOWED_HOSTS = ['hadhuub.com','www.hadhuub.com','hadhuub-production.up.railway.app']

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        config('ALLOWED_HOSTS','').split(','),
    )
)


DEBUG = False

# INSTALLED_APPS +=[
#     'django.contrib.postgres',
# ]
SECRET_KEY = config('SECRET_KEY')


# DATABASES = {
#      'default': {
#      'ENGINE': 'django.db.backends.postgresql',
#      'NAME': config('NAME'),
#      'USER': config('USER'),
#      'PASSWORD': config('PASSWORD'),
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
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# #HTTPS  settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True


# #HSTS settings
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
