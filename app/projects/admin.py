from django.contrib import admin
from .models import OurProjects, MainProjects, AmericanCorner
from modeltranslation.admin import TranslationAdmin
from .translation import *

@admin.register(OurProjects)
class OurProjectsAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru', 'title_2_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky', 'title_2_ky')}),
        ('Фотография', {
            'fields': ['image', 'created_at'],
        }),
    )
@admin.register(MainProjects)
class MainProjectsAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky')}),
        ('Фотография', {
            'fields': ['image', 'created_at'],
        }),
    )
@admin.register(AmericanCorner)
class AmericanCornerAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {'fields': ('title_ru', 'description_ru')}),
        ("Кыргызская версия", {'fields': ('title_ky', 'description_ky')}),
        ('Фотография', {
            'fields': ['image', 'created_at'],
        }),
    )