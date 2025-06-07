from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, ServiceCategory, ServiceHeader
from modeltranslation.admin import TranslationAdmin
from .translation import *

class ServiceCategoryAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['name_ky']
        }),
        ('Русская версия', {
            'fields': ['name_ru']
        })
    )
admin.site.register(ServiceCategory, ServiceCategoryAdmin)

class ServiceAdmin(TranslationAdmin):
    fieldsets = (
        ('Кыргызская версия', {
            'fields': ['category_ky', 'title_ky', 'description_ky'],
        }),
        ('Русская версия', {
            'fields': ['category_ru', 'title_ru', 'description_ru']
        }),
        ('Изображения', {
            'fields': ['image']
        })
    )
admin.site.register(Service, ServiceAdmin)

@admin.register(ServiceHeader)
class ServiceHeaderAdmin(TranslationAdmin):
    fieldsets = (
        ('Тексты', {
            'fields': ('title_ru', 'title_ky', 'description_ru', 'description_ky')
        }),
        ('Изображения', {
            'fields': ('image1', 'image2', 'image3')
        }),
    )
    list_display = ('title',)
