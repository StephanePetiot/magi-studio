# from django.core.validators import FileExtensionValidator
# from django.db import models
# from django.urls import reverse

# from app.common.models import BaseModel


# class GameSession(BaseModel):
#     ALLOWED_EXTENSIONS = [
#         "csv",
#     ]

#     class Gender(models.TextChoices):
#         BOY = "boy", "Boy"
#         GIRL = "girl", "Girl"
#         MAN = "man", "Man"
#         WOMAN = "woman", "Woman"
#         TRANSGENDER = "transgender", "Transgender"
#         NON_BINARY = "non_binary", "Non-binary"
#         OTHER = "other", "Other"
#         NO_ANSWER = "no_answer", "No answer"

#     ADULT_AGE_SPAN_CHOICES = [
#         ("18-25", "18-25 years old"),
#         ("26-35", "26-35 years old"),
#         ("36-45", "36-45 years old"),
#         ("46-55", "46-55 years old"),
#         ("56-65", "56-65 years old"),
#         ("66-75", "66-75 years old"),
#         ("76-85", "76-85 years old"),
#         ("older", "older"),
#     ]

#     class LevelOfEducation(models.TextChoices):
#         NO_DIPLOMAS = "no_diplomas", "No diplomas"
#         MIDDLE_SCHOOL_DIPLOMA = "middle_school_diploma", "Middle school diploma"
#         TECHNICAL_DIPLOMA = "technical_diploma", "Technical diploma (CAP, BEP, etc.)"
#         HIGH_SCHOOL_DIPLOMA = "high_school_diploma", "High school diploma"
#         UNDERGRADUATE = "undergraduate", "Undergraduate"
#         SUPERIOR_TECHNICAL_DIPLOMA = "superior_technical_diploma", "Superior technical diploma (DUT, BTS, etc.)"
#         LICENSE_OR_BACHELOR = "license_or_bachelor", "License, bachelor or equivalent"
#         MASTER = "master", "Master or equivalent"
#         PHD = "phd", "PhD"
#         OTHER = "other", "Other"
#         NO_ANSWER = "no_answer", "No answer"

#     class FirstTimePlaying(models.TextChoices):
#         NEVER = "never", "Never"
#         ONCE = "once", "Once"
#         MORE_THAN_ONCE = "more_than_once", "More than once"

#     class ResultChoices(models.TextChoices):
#         SIMILARITY = "similarity", "Similarity"
#         RULE = "rule", "Rule"
#         ERROR = "error", "Error"

#     gender = models.CharField(max_length=32, choices=Gender.choices)
#     child_age = models.PositiveSmallIntegerField(blank=True, null=True)
#     adult_age_span = models.CharField(max_length=32, choices=ADULT_AGE_SPAN_CHOICES, blank=True, null=True)
#     level_of_education = models.CharField(max_length=32, choices=LevelOfEducation.choices, blank=True, null=True)
#     first_time_playing = models.CharField(max_length=32, choices=FirstTimePlaying.choices)

#     rule = models.CharField(max_length=32)

#     answers = models.FileField(
#         upload_to="answers",
#         blank=True,
#         null=True,
#         validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)],
#     )

#     feedback = models.JSONField(default="", blank=True, null=True)
#     result = models.CharField(max_length=32, choices=ResultChoices.choices, blank=True, null=True)
#     error_log = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.id}, {self.created_at}"

#     def get_absolute_url(self):  # Returns the absolute URL of the results
#         return reverse("core:session", kwargs={"id": self.id})

#     class Meta:
#         verbose_name = "Game session"
#         verbose_name_plural = "Game sessions"
