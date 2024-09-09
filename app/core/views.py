import json

from constance import config
from django.shortcuts import render
from django.views import View

from .selectors import project_list


class IndexView(View):
    def get(self, request, *args, **kwargs):
        projects = [
            {
                "title": project.title,
                "subtitle": project.subtitle,
                "description": project.description,
                "picture": project.picture.url if project.picture else None,
            }
            for project in project_list()
        ]

        return render(
            request,
            "core/index.html",
            {
                "banner_path": config.LANDING_BANNER,
                "landing_subtitle": config.LANDING_SUBTITLE,
                "translation_text": config.TRANSLATION_TEXT,
                "lettering_text": config.LETTERING_TEXT,
                "correction_text": config.CORRECTION_TEXT,
                "graphism_text": config.GRAPHISM_TEXT,
                "edition_text": config.EDITION_TEXT,
                "studio_first_paragraph": config.STUDIO_FIRST_PARAGRAPH,
                "studio_second_paragraph": config.STUDIO_SECOND_PARAGRAPH,
                "studio_third_paragraph": config.STUDIO_THIRD_PARAGRAPH,
                "studio_fourth_paragraph": config.STUDIO_FOURTH_PARAGRAPH,
                "studio_fifth_paragraph": config.STUDIO_FIFTH_PARAGRAPH,
                "studio_bottom_text": config.STUDIO_BOTTOM_TEXT,
                "contact_content": config.CONTACT_CONTENT,
                "projects": json.dumps(projects),
            },
        )


class LegalView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/legal.html", {})
