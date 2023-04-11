# Django HTTP requests handlers
from django.shortcuts import render
from django.conf import settings

from constance import config

def index(request):
    cover_image_url = f"{settings.MEDIA_URL}{config.COVER_IMAGE}"
    print(cover_image_url)
    return render(request, 'core/index.html', { 'cover_image_url': cover_image_url })

def legal(request):
    return render(request, 'core/legal.html')