# from app.users.models import BaseUser
#from django.contrib.auth.models import User

def user_get_login_data(*, user):
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
        "is_superuser": user.is_superuser,
    }
