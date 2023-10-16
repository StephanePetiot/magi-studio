import os

from .base import *  # noqa

DEBUG = bool(int(os.environ.get("DJANGO_DEBUG", 0)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
USE_X_FORWARDED_HOST = True

CORS_ALLOW_ALL_ORIGINS = False
CSRF_TRUSTED_ORIGINS = ["https://3ia-demos.inria.fr", "https://www.3ia-demos.inria.fr"]

ROOT_URL = os.environ.get("ROOT_URL", "")
FORCE_SCRIPT_NAME = ROOT_URL + "/"
SESSION_COOKIE_PATH = ROOT_URL + "/"
SESSION_COOKIE_NAME = "magi-studio-sessionid"

LOGIN_URL = ROOT_URL + LOGIN_URL  # noqa
LOGIN_REDIRECT_URL = ROOT_URL + LOGIN_REDIRECT_URL  # noqa
LOGOUT_REDIRECT_URL = ROOT_URL + LOGOUT_REDIRECT_URL  # noqa

STATIC_URL = ROOT_URL + STATIC_URL  # noqa
MEDIA_URL = ROOT_URL + MEDIA_URL  # noqa
