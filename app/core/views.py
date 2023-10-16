import json
import os

from constance import config
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        cover_image_url = os.path.join(settings.MEDIA_URL, config.COVER_IMAGE)
        return render(request, 'core/index.html', { 'cover_image_url': cover_image_url })


class LegalView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/legal.html", {})
