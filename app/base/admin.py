from django.contrib import admin
from app.base.models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from .translation import *
from django.forms import ModelForm, BaseInlineFormSet
# Register your models here.

class LogoAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {"fields": ("title_ru", 'description_ru')}),
        ("Кыргызская версия", {"fields": ("title_ky", 'description_ky')}),
        ("Изображения", {"fields": ("image_1", "image_2", "image_3", "image_4", "image_5")}),
    )

admin.site.register(Logo, LogoAdmin)


class CatalogsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Изображния', {
            'fields': ['image'],
        }),
    )
admin.site.register(Catalogs, CatalogsAdmin)




#Алишер
class WeOfferViewingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru','selections_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky','selections_ky', 'description_ky')
        }),
        ('Изображения', {
            'fields': ['link', 'video'],
        }),
       
    )
admin.site.register(WeOfferViewing, WeOfferViewingAdmin)


class PartnerImageInline(admin.TabularInline):
    model = PartnerImage
    extra = 3
    fields = ("image", "image_preview", "links")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit:cover;" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью"


class PartnersAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {"fields": ("title_ru",)}),
        ("Кыргызская версия", {"fields": ("title_ky",)}),
    )

    inlines = [PartnerImageInline]

    list_display = ("title_ru", "preview_images", "preview_links")

    def preview_links(self, obj):
        links = obj.partner_images.exclude(links__isnull=True).exclude(links__exact='')
        if links.exists():
            return format_html("<br>".join(
                f'<a href="{img.links}" target="_blank">Ссылка {i+1}</a>'
                for i, img in enumerate(links[:3])
            ))
        return "Нет ссылок"

    def preview_images(self, obj):
        images = obj.partner_images.all()[:3]
        if images:
            return format_html(
                "".join(f'<img src="{img.image.url}" width="50" height="50" style="margin-right:5px;"/>' for img in images)
            )
        return "Нет изображений"

    preview_images.short_description = "Превью"
    preview_links.short_description = "Ссылки"

admin.site.register(Partners, PartnersAdmin)


  
class ReadingRatingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'place_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'place_ky', 'description_ky')
        }),
        ("Изображение", {
            'fields': ('images',)
        }),
    )
admin.site.register(ReadingRating, ReadingRatingAdmin)   

  

class BooksRatingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'place_ru', 'book_ru', 'author_ru', 'code_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'place_ky', 'book_ky', 'author_ky', 'code_ky')
        }),
        ("Изображение", {
            'fields': ('image',)
        }),
    )

admin.site.register(BooksRating, BooksRatingAdmin)


class HeaderFooterAdmin(TranslationAdmin):
    fieldsets = (    
        ("Русская версия", {
            'fields': ('header_ru', 'footer_ru', 'logo_ru', 'name_ru', 'address_ru', 'icons_ru',
                       'about_library_ru', 'supports_ru', 'news_ru', 'services_ru', 'catalog_ru',
                       'afisha_ru', 'pro_activity_ru', 'page_for_readers_ru', 'el_library_ru', 'projects_ru',
                       'phone_number_ru', 'title_about_library_ru', 'title_afisha_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('header_ky', 'footer_ky', 'logo_ky', 'name_ky', 'address_ky', 'icons_ky',
                       'about_library_ky', 'supports_ky', 'news_ky', 'services_ky', 'catalog_ky',
                       'afisha_ky', 'pro_activity_ky', 'page_for_readers_ky', 'el_library_ky', 'projects_ky',
                       'phone_number_ky', 'title_about_library_ky', 'title_afisha_ky',)
        }),
        ("Изображение", {
            'fields': ('instagram_icon','instagram_icon_url', 'facebook_icon', 'facebook_icon_url', 'google_icon', 'google_icon_url', 'youtube_icon', 'youtube_icon_url',)
        }),
    )
    def image_tag(self, obj):
        if obj.instagram_icon:
            return f'<a href="{obj.instagram_icon_url}" target="_blank"><img src="{obj.instagram_icon.url}" width="30" height="30" /></a>'
        return "Нет иконки Instagram"
    image_tag.short_description = 'Instagram Icon'

    def facebook_image_tag(self, obj):
        if obj.facebook_icon:
            return f'<a href="{obj.facebook_icon_url}" target="_blank"><img src="{obj.facebook_icon.url}" width="30" height="30" /></a>'
        return "Нет иконки Facebook"
    facebook_image_tag.short_description = 'Facebook Icon'

    def google_image_tag(self, obj):
        if obj.google_icon:
            return f'<a href="{obj.google_icon_url}" target="_blank"><img src="{obj.google_icon.url}" width="30" height="30" /></a>'
        return "Нет иконки Google"
    google_image_tag.short_description = 'Google Icon'

    def youtube_image_tag(self, obj):
        if obj.youtube_icon:
            return f'<a href="{obj.youtube_icon_url}" target="_blank"><img src="{obj.youtube_icon.url}" width="30" height="30" /></a>'
        return "Нет иконки YouTube"
    youtube_image_tag.short_description = 'YouTube Icon'


    def logo_image(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="50" height="50" />'
        return 'Нет логотипа'
    logo_image.short_description = 'Логотип'
    
    def icons_image(self, obj):
        if obj.icons:
            return f'<img src="{obj.icons.url}" width="50" height="50" />'
        return 'Нет иконок'
    icons_image.short_description = 'Иконки'

    def image_tag(self, obj):
        if obj.instagram_icon:
            return f'<img src="{obj.instagram_icon.url}" width="30" height="30" />'
        return "Нет иконки Instagram"
    image_tag.short_description = 'Instagram Icon'

admin.site.register(HeaderFooter, HeaderFooterAdmin)

class RegisterLogoutAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_reg_ru', 'description_reg_ru', 'title_log_ru', 'description_log_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_reg_ky', 'description_reg_ky', 'title_log_ky', 'description_log_ky')
        }),
        ("Изображение", {
            'fields': ('image_reg',)
        }),
    )

admin.site.register(RegisterLogout, RegisterLogoutAdmin)
