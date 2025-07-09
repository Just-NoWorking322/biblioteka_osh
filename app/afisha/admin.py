from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .translation import *

# Register your models here.

@admin.register(Afisha)
class AfishaAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображение', {
            'fields': ['image',],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'title_2_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'title_2_ky'],
        }),
    )

    

    