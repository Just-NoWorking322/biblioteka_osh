from modeltranslation.translator import TranslationOptions, register
from app.page_for_readers.models import Banner, Graphic_work, Titles, ReadBase, Appointment

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(Graphic_work)
class GraphicWorkTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(ReadBase)
class ReadBaseTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )

@register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'hosts',
        'schedule',
    )

@register(Titles)
class TitlesTranslationOptions(TranslationOptions):
    fields = (
        "work",
        "citizens",
        "hall",
        'readers',
        'books',
    )





