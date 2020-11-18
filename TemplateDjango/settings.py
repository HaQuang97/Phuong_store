"""
Django settings for HatarakiNurse project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import datetime
import os

from decouple import RepositoryEnv, Config
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.environ.get('ENVIRONMENT')
project_environment = env if env else 'development'
ENV_FILE = os.path.join(BASE_DIR, '.env/.{}'.format(project_environment))
env_config = Config(RepositoryEnv(ENV_FILE))

SECRET_KEY = env_config.get('SECRET_KEY')
ALLOWED_HOSTS = env_config.get('ALLOWED_HOSTS')
DEBUG = env_config.get('DEBUG') == "True"
SILK_ENABLE = env_config.get('SILK_ENABLE') == 'True'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'apps.authentication',
    'apps.cms_admin',
    'imagekit',
    'drf_yasg',
]

# Imagekit config
IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'apps.utils.util_function.FixJustInTime'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

if SILK_ENABLE:
    INSTALLED_APPS += [
        'silk',
    ]
    MIDDLEWARE += [
        'silk.middleware.SilkyMiddleware',
    ]

ROOT_URLCONF = 'TemplateDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'TemplateDjango.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = env_config('LANGUAGE_CODE')

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=1440),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(minutes=1440),
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_AUTH_COOKIE': 'jwt_auth_token'
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.authentication.utils.custom_auth.CustomAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'EXCEPTION_HANDLER': 'apps.utils.exception_handler.custom_exception_handler',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'apps.utils.display_edit_forms.BrowsableAPIRendererWithoutForms',
    ),
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env_config('POSTGRES_DB'),
        'USER': env_config('POSTGRES_USER'),
        'PASSWORD': env_config('POSTGRES_PASSWORD'),
        'HOST': env_config('DATABASE_HOST'),
        'PORT': env_config('DATABASE_PORT'),
    }
    
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': reverse_lazy('admin:login'),
    'LOGOUT_URL': '/admin/logout',
    'PERSIST_AUTH': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'REFETCH_SCHEMA_ON_LOGOUT': True,
    'DEFAULT_INFO': 'SpaceShare.urls.swagger.swagger_info',
    
    'SECURITY_DEFINITIONS': {
        'JWT': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'DOC_EXPANSION': 'none',
    
}

AUTH_USER_MODEL = 'authentication.User'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'handlers': ['file', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s  %(asctime)s  %(module)s '
                      '%(process)d  %(thread)d  %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        '': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
DATE_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')
BIRTHDAY_FORMATS = ('%m-%Y', '%Y-%m')
DATE_TIME_FORMATS = ('%d-%m-%Y %H:%M:%S', '%d/%m/%Y')
