from modeltranslation.translator import register, TranslationOptions
from .models import LibrarySupport, LibraryValue, LibraryTitles

@register(LibrarySupport)
class LibrarySupportTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    

@register(LibraryValue)
class LibraryValueTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description')


@register(LibraryTitles)
class LibraryTitlesTranslationOptions(TranslationOptions):
    fields = ('title_1', 'title_2', 'title_3',  'left_description', 'right_description')
