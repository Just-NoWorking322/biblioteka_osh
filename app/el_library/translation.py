from modeltranslation.translator import register, TranslationOptions
from app.el_library.models import Book

@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'description')  

# @register(Partner)
# class PartnerTranslationOptions(TranslationOptions):
#     fields = ('title',)  