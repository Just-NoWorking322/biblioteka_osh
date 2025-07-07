from modeltranslation.translator import register, TranslationOptions
from .models import News, DailyNews, EventsNews, BookArrival, Catalog, MediaCoverage

@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(DailyNews)
class DailyNewsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'detailed_description', 'date')
    
@register(EventsNews)
class EventsNewsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'detailed_description', 'time')

@register(BookArrival)
class BookArrivalTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'author')

@register(Catalog)
class SpecialBookArrivalTranslationOption(TranslationOptions):
    fields = ('title' ,'author', 'special_feature', 'note')

@register(MediaCoverage)
class MediaCoverageTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'coverage_period')