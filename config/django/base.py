import os

from config.env import BASE_DIR

SECRET_KEY = os.environ.get('SECRET_KEY', "indago")

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 1)))

ALLOWED_HOSTS = ['*']

# Apps on which to operate database migrations
LOCAL_APPS = [
    'app.authentication.apps.AuthenticationConfig',
    'app.api.apps.ApiConfig',
    'app.users.apps.UsersConfig',
    'app.emails.apps.EmailsConfig',
    'app.core.apps.CoreConfig',
]

THIRD_PARTY_APPS = [
    "rest_framework",           # DRF
    'webpack_loader',           # Django webpack loader for static files synchronization
    'django.contrib.humanize',  # For template tags
    'corsheaders',              # Development-specific apps for CORS handling
    'constance'                 # Django dynamic settings
]

INSTALLED_APPS = [
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,

    # Django default apps (admin interface, authentication system, data models/sessions/messages/static files handler)
    'django.contrib.admin',    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware components, for several purposes
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = 'config.asgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': f"-c search_path=\"{ os.environ['DB_SCHEMA'] }\""
        },
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'database',
        'PORT': 5432,
    }
}

# Authentication parameters
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
PASSWORD_RESET_TIMEOUT = 3600
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Language and date parameters
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True

# Static and media files URLs
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build'),
]
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000

# TO DO When the DRF is set up
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'   # Automatic incrementation for primary key fields in the tables

from config.settings.cors import *
from config.settings.email_sending import *
from config.settings.markdownify import *
from config.settings.webpack import *
from config.settings.constance import *

# TO DO When the Debug toolbar is set up
""" from config.settings.debug_toolbar.settings import *  # noqa
from config.settings.debug_toolbar.setup import DebugToolbarSetup  # noqa """

""" INSTALLED_APPS, MIDDLEWARE = DebugToolbarSetup.do_settings(INSTALLED_APPS, MIDDLEWARE) """