from django.urls import include, path

app_name = "api"
urlpatterns = [path("", include("app.core.endpoints"))]
