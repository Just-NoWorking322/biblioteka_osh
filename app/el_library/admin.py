from django.contrib import admin
from app.el_library.models import Book
from app.el_library.translation import *
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html

class BookAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'author_ru', 'description_ru',],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky','author_ky', 'description_ky',],
        }),
        ('Глобальные настройки', {'fields': ['image', 'file', 'link']}),
    )
    list_display = ('title_ky', 'title_ru', 'author')



admin.site.register(Book, BookAdmin)



# class PartnerImageInline(admin.TabularInline):
#     model = PartnerImage
#     extra = 3
#     fields = ("image", "image_preview")
#     readonly_fields = ("image_preview",)

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="100" height="100" style="object-fit:cover;" />', obj.image.url)
#         return "Нет изображения"

#     image_preview.short_description = "Превью"


# class PartnersAdmin(TranslationAdmin):
#     fieldsets = (
#         ("Русская версия", {"fields": ("title_ru",)}),
#         ("Кыргызская версия", {"fields": ("title_ky",)}),
#     )

#     inlines = [PartnerImageInline]

#     list_display = ("title_ru", "preview_images")

#     def preview_images(self, obj):
#         images = obj.partner_images.all()[:3]
#         if images:
#             return format_html(
#                 "".join(f'<img src="{img.image.url}" width="50" height="50" style="margin-right:5px;"/>' for img in images)
#             )
#         return "Нет изображений"

#     preview_images.short_description = "Превью"

# admin.site.register(Partner, PartnersAdmin)
