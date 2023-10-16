from django.urls import path

from .views import IndexView, LegalView

app_name = "core"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("legal", LegalView.as_view(), name="legal"),
]
