from modeltranslation.translator import TranslationOptions, register

from .models import Afisha

@register(Afisha)
class AfishaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'title_2')



