from modeltranslation.translator import TranslationOptions, register
from .models import Service, ServiceCategory, ServiceHeader

@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # Поле для перевода

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('category', 'title', 'description')  # Поля для перевода

@register(ServiceHeader)
class ServiceHeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # Поля для перевода
