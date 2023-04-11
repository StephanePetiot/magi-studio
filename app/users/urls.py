from django.urls import path

from .views import UsersRegisterView, UsersPasswordResetView, UsersPasswordResetConfirmView, UsersPasswordResetCompleteView

app_name = 'users'
urlpatterns = [
    path('register', UsersRegisterView.as_view(), name = 'register'),
    path('reset_password/', UsersPasswordResetView.as_view(), name = 'password_reset'),
    path('reset/<uidb64>/<token>', UsersPasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset_password_complete/', UsersPasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]
