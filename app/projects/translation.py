from modeltranslation.translator import register, TranslationOptions
from .models import OurProjects, MainProjects, AmericanCorner

@register(OurProjects)
class OurProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'title_2')

@register(MainProjects)
class MainProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

