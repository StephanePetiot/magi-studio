import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.base")

app = Celery("magi-studio")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
