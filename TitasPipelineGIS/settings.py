"""
Django settings for TitasPipelineGIS project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
environ.Env.read_env(os.path.join(BASE_DIR / 'TitasPipelineGIS', '.env'))
ON_PRODUCTION = os.getenv('ON_PRODUCTION', 'False') == "True"

if ON_PRODUCTION:
    # porduction
    GEOS_LIBRARY_PATH = '/usr/lib/x86_64-linux-gnu/libgeos_c.so'
    GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'
else:
    # GDAL configuration
    GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal304'
    VENV_BASE = os.environ['VIRTUAL_ENV']
    if os.name == 'nt':
        import platform
        OSGEO4W = r"C:\OSGeo4W"
        # if '64' in platform.architecture()[0]:
        #     OSGEO4W += "64"
        # assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
        os.environ['OSGEO4W_ROOT'] = OSGEO4W
        os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
        os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
        os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Gis config
    'django.contrib.gis',
    # libraries
    'leaflet',
    'rest_framework',
    'django_resized',
    'phonenumber_field',
    'phonenumbers',
    'crispy_forms',
    # cors
    'corsheaders',
    # installed app
    'AuthenticationApp',
    'GIS_APP',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TitasPipelineGIS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TitasPipelineGIS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': '5432'
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# last one 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'mygeoproject',
#         'USER': 'mygeoprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'Geoproject',
#         'USER': 'Geoprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'titas_pipeline_v1',
#         'USER': 'gis_auth',
#         'PASSWORD': 'pranto@123',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }


# clean one 
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mygproject',
        'USER': 'mygprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath("static"),
]
# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'AuthenticationApp.User'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True

#sendgrid

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'

# check sendinblue 
# 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
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
DEFAULT_FROM_EMAIL = 'shafiqwish@gmail.com'


ENC_KEY = env('ENC_KEY')
CORS_ORIGIN_ALLOW_ALL = True
# SECURE_CROSS_ORIGIN_OPENER_POLICY = None
#if ON_PRODUCTION:
 #   SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
  #  SECURE_SSL_REDIRECT = True
