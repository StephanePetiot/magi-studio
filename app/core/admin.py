import csv
import io
import zipfile

from django.contrib import admin
from django.http import HttpResponse

admin.site.site_header = "Magi Studio"


""" @admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = (
        "gender",
        "child_age",
        "adult_age_span",
        "level_of_education",
        "first_time_playing",
        "rule",
        "answers",
        "feedback",
        "result",
        "error_log",
        "created_at",
    )
    list_filter = (
        "gender",
        "child_age",
        "adult_age_span",
        "level_of_education",
        "first_time_playing",
        "result",
        "created_at",
    )
    readonly_fields = (
        "gender",
        "child_age",
        "adult_age_span",
        "level_of_education",
        "first_time_playing",
        "rule",
        "answers",
        "feedback",
        "result",
        "error_log",
        "created_at",
    )
 """