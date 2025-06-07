from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import LibrarySupport, LibraryValue, LibraryTitles, Pay
from .translations import *

@admin.register(LibrarySupport)
class LibrarySupportAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky')}),
        ('Фотография', {
            'fields': ['image'],
        }),
    )

@admin.register(LibraryValue)
class LibraryValueAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'short_description_ru', 'full_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'short_description_ky', 'full_description_ky')}),
        ('Иконка', {
            'fields': ['icon'],
        }),
    )

@admin.register(LibraryTitles)
class LibraryTitlesAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_1_ru', 'title_2_ru', 'title_3_ru', 'left_description_ru', 'right_description_ru')}),
        ("Кыргызская версия", {'fields': ('title_1_ky', 'title_2_ky', 'title_3_ky', 'left_description_ky', 'right_description_ky')}),
    )

admin.site.register(Pay)