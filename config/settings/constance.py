CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'COVER_IMAGE': ('otter-large.png', 'Cover Picture', 'image_field'),
}