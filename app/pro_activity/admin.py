from django.contrib import admin
from app.pro_activity.models import Activity, TypeActivity
from modeltranslation.admin import TranslationAdmin
from .translations import *


class ActivityAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'description_details_ru', 'links', 'type_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'description_details_ky', 'type_ky'],
        }),
    )

admin.site.register(Activity, ActivityAdmin)

admin.site.register(TypeActivity)