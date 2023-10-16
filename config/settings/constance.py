from django.core.validators import FileExtensionValidator

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    "image_field": [
        "django.forms.ImageField",
        {"validators": [FileExtensionValidator(allowed_extensions=["png", "jpg"])]},
    ],
}

CONSTANCE_CONFIG = {
    "COVER_IMAGE": ("otter-large.png", "Cover Picture", "image_field"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    # "Visuals when value is 0": ("HEAD_0", "BODY_0", "PROPELLERS_0", "FLAMES_0"),
}
