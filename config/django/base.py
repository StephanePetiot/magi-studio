import os
from django.utils.translation import gettext_lazy as _

from config.env import BASE_DIR

SECRET_KEY = os.environ.get("SECRET_KEY", "")

DEBUG = bool(int(os.environ.get("DJANGO_DEBUG", 1)))

ALLOWED_HOSTS = ["*"]

# Apps on which to operate database migrations
LOCAL_APPS = [
    "app.core.apps.CoreConfig",
    "app.common.apps.CommonConfig",
    "app.authentication.apps.AuthenticationConfig",
    "app.tasks.apps.TasksConfig",
    "app.api.apps.ApiConfig",
    "app.users.apps.UsersConfig",
    "app.emails.apps.EmailsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "webpack_loader",  # Django webpack loader for static files synchronization
    "daphne",  # Django channels for asynchronous requests
    "corsheaders",  # Development-specific apps for CORS handling
    "constance",  # Global dynamic preferences
    "constance.backends.database",
]

INSTALLED_APPS = [
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
    # Django default apps (admin interface, authentication system, data models/sessions/messages/static files handler)
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Middleware components, for several purposes
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "frontend", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "constance.context_processors.config",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", ""),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", "database"),
        "PORT": os.environ.get("POSTGRES_PORT", 5432),
    }
}

# Authentication parameters
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
PASSWORD_RESET_TIMEOUT = 3600
LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

AUTH_USER_MODEL = "users.BaseUser"

# Language and date parameters
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("en", _("English")),
    ("fr", _("French")),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "assets", "locales"),
]

# Static and media files URLs
STATIC_URL = os.environ.get("STATIC_URL", "/static/")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend", "build"),
]
STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, "static"))

MEDIA_URL = os.environ.get("MEDIA_URL", "/media/")
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "app.api.exception_handlers.drf_default_with_modifications_exception_handler",
    # 'EXCEPTION_HANDLER': 'app.api.exception_handlers.hacksoft_proposed_exception_handler',
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend"),
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Automatic incrementation for primary key fields in the tables

from config.settings.celery import *  # noqa
from config.settings.channels import *  # noqa
from config.settings.cors import *  # noqa
from config.settings.email_sending import *  # noqa
from config.settings.webpack import *  # noqa
from config.settings.sessions import *  # noqa
from config.settings.constance import *  # noqa

from config.settings.debug_toolbar.settings import *  # noqa
from config.settings.debug_toolbar.setup import DebugToolbarSetup  # noqa

INSTALLED_APPS, MIDDLEWARE = DebugToolbarSetup.do_settings(INSTALLED_APPS, MIDDLEWARE)
