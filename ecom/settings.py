import os
from pathlib import Path

# import django_heroku
# import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'django-insecure-o8x581e+e#i@)w#i0tg(loir14s8(b7f936%)qcwt_4!p&r*&&'
# DEBUG = True
DEBUG = False
ALLOWED_HOSTS = ['https://waseemint.com/','waseemint.com','waseem-int-d368a88e8f0a.herokuapp.com','www.waseemint.com','127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    #   "corsheaders",

    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'customkit',
    'images',
    'youtube',
    'ads',
    'widget_tweaks',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_session_timeout.middleware.SessionTimeoutMiddleware",

]

SESSION_EXPIRE_SECONDS = 36000
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "category.context_processors.categories_processor",
                "carts.context_processors.counter",
                "store.context_processors.products",

            ],
        },
    },
]


WSGI_APPLICATION = 'ecom.wsgi.application'
AUTH_USER_MODEL = "accounts.Account"



# DATABASES = { 
#     'default': { 
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', 
#         'NAME': os.environ.get('NAME'), 
#         'USER': os.environ.get('USER'), 
#         'PASSWORD': os.environ.get('DB_PASSWORD'), 
#         'HOST': os.environ.get('HOST'), 
#         'PORT': '5432', 
#     } 
# }

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'dejdlbdf7mcu43', 
        'USER': 'uqtmvgh987aqi', 
        'PASSWORD': 'p1bb530f5b03418c9e092f6c98dc7d9ba1b5a301650bc1290d5876c96fe77dbbf', 
        'HOST': 'c9uss87s9bdb8n.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com', 
        'PORT': '5432', 
    } 
} 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_TZ = True


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# WHITENOISE_USE_FINDERS = True

# # Add this for serving media files
# from whitenoise import WhiteNoise
# import os

# application = WhiteNoise(application)
# media_root = os.path.join(BASE_DIR, 'media')
# application.add_files(media_root, prefix='/media/')


# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR,'static'),
# )
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# if DEBUG:
# else:
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



ADMINS = [
    ('Waseem Ahmed', 'waseemint.pk@gmail.com'),
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
# DEFAULT_EMAIL
DEFAULT_FROM_EMAIL = 'waseemint.pk@gmail.com'
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_EMAIL')
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('DEFAULT_EMAIL')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'waseemint.pk@gmail.com'
EMAIL_HOST_PASSWORD = 'pgkzlwobwbbfzhky'



SESSION_ENGINE = 'django.contrib.sessions.backends.db'  
SESSION_COOKIE_SECURE = False

# django_heroku.settings(locals())
