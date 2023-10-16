from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from app.users.models import BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_superuser", "is_active", "created_at", "updated_at")

    readonly_fields = (
        "created_at",
        "updated_at",
    )
