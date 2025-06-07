from django.contrib import admin
from app.page_for_readers.models import Banner, Graphic_work, Titles, Appointment, ReadBase
from modeltranslation.admin import TranslationAdmin
from .translations import *

class BannerAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Основа', {
            'fields': ['image', 'links'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', ],
        }),
    )

admin.site.register(Banner, BannerAdmin)

class Graphic_workAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', ],
        }),
    )

admin.site.register(Graphic_work, Graphic_workAdmin)
class ReadBaseAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky'],
        }),
        ('Ссылка на видео', {
            'fields': ['link'],
        }),
    )

admin.site.register(ReadBase, ReadBaseAdmin)

class AppointmentAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru', 'hosts_ru', 'schedule_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'hosts_ky', 'schedule_ky'],
        }),
    )

admin.site.register(Appointment, AppointmentAdmin)


class TitlesAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['work_ru', 'citizens_ru', 'hall_ru', 'readers_ru', 'books_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['work_ky', 'citizens_ky', 'hall_ky', 'readers_ky', 'books_ky' ],
        }),
    )

admin.site.register(Titles, TitlesAdmin)

