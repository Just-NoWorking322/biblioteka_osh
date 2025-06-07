from django.contrib import admin
from app.news.models import *
from app.news.translation import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class NewsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Изображения', {
            'fields': ['left_image', 'middle_image', 'dextral_image'],
        }),
    )


admin.site.register(News, NewsAdmin)



class DailyNewsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'detailed_description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'detailed_description_ky'],
        }),
        ('Изображения и время', {
            'fields': ['image', 'date'],
        }),
    )

admin.site.register(DailyNews, DailyNewsAdmin)

class EventsNewsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'detailed_description_ru', 'time_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'detailed_description_ky', 'time_ky'],
        }),
        ('Изображения', {
            'fields': ['image'],
        }),
    )

admin.site.register(EventsNews, EventsNewsAdmin)

class BookArrivalAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {'fields': ['title_ru', 'description_ru', 'author_ru']}),
        ('Кыргызская версия', {'fields': ['title_ky', 'description_ky', 'author_ky']}),
        ('Глобальные настройки', {'fields': ['image', 'file', 'link', 'populars']}),
    )

admin.site.register(BookArrival, BookArrivalAdmin)

class CatalogAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {'fields': ['title_ru', 'note_ru', 'author_ru']}),  
        ('Кыргызская версия', {'fields': ['title_ky', 'note_ky', 'author_ky']}),  
        ('Все - Популярное', {'fields': ['popular', 'read_count']}),
    )

admin.site.register(Catalog, CatalogAdmin)

class MediaCoverageAdmin(TranslationAdmin):

    fieldsets = (
        ('Русская версия', { 
            'fields': ['title_ru', 'description_ru', 'coverage_period_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'coverage_period_ky'],
        }),
        ('Глобальные настройки', {
            'fields': ['image', 'link'],
    
        }),
    )
    
admin.site.register(MediaCoverage, MediaCoverageAdmin)


