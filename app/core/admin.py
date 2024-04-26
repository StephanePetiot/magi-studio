from django.contrib import admin

from .models import Project

admin.site.site_header = "Magi Studio"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = (
        "title",
        "subtitle",
        "description",
        "picture",
        "updated_at",
        "created_at",
    )

    readonly_fields = (
        "updated_at",
        "created_at",
    )
