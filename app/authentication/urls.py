from django.urls import include, path

from django.contrib.auth.views import LoginView, LogoutView
from .views import UserSessionLoginView

app_name = 'authentication'
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name = 'authentication/login.html',
            redirect_authenticated_user = True
        ),
        name = "login"),
    path(
        "logout/",
        LogoutView.as_view(),
        name = "logout"
    ),
]