from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from app.core import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),

    path("auth/", include("app.authentication.urls", namespace = 'authentication')),
    
    path('', include('app.core.urls', namespace = 'core')),

    path('api/', include('app.api.urls', namespace = 'api')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

""" from config.settings.debug_toolbar.setup import DebugToolbarSetup  # noqa

urlpatterns = DebugToolbarSetup.do_urls(urlpatterns) """