import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 0)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(' ')
USE_X_FORWARDED_HOST = True

CORS_ALLOW_ALL_ORIGINS = False