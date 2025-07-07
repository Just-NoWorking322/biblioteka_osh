from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from app.about_library.translation import *
from app.about_library.models import AboutLibrary, TitlesLibrary, Management, StructureAndLibraries, Acts, History


class AboutLibraryAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_1_ru', 'title_2_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_1_ky', 'title_2_ky', 'description_ky'],
        }),
        ('Изображения', {
            'fields': ['image_1', 'image_2', 'image_3'],
        }),
    )

admin.site.register(AboutLibrary, AboutLibraryAdmin)

class TitlesLibraryAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_1_ru', 'title_2_ru', 'title_3_ru', 'title_4_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_1_ky', 'title_2_ky', 'title_3_ky', 'title_4_ky'],
        }),
    )
    
admin.site.register(TitlesLibrary, TitlesLibraryAdmin)

class ManagementAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['role_ru', 'full_name_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['role_ky', 'full_name_ky'],
        }),
        ('Изображения', {
            'fields': ['image',],
        }),
    )
    
admin.site.register(Management, ManagementAdmin)

class StructureAndLibrariesAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['image_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['image_ky'],
        }),
    )
    
admin.site.register(StructureAndLibraries, StructureAndLibrariesAdmin)

class ActsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Изображения', {
            'fields': ['link'],
        }),
    )

admin.site.register(Acts, ActsAdmin)

class HistoryAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Изображения', {
            'fields': ['image'],
        }),
    )

admin.site.register(History, HistoryAdmin)
