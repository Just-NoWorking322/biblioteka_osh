from modeltranslation.translator import TranslationOptions, register
from app.pro_activity.models import Activity, TypeActivity


@register(Activity)
class ActivityTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
        'description_details',
        'type',
    )

@register(TypeActivity)
class TypeActivityTranslationOptions(TranslationOptions):
    fields = (
        'type',
    )