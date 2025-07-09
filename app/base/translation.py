from modeltranslation.translator import register, TranslationOptions
from app.base.models import *


@register(Logo)
class LogoTranslation(TranslationOptions):
    fields = ('title', 'description',)


@register(Catalogs)
class CatalogsTranslation(TranslationOptions):
    fields = ('title', 'description')
    


@register(WeOfferViewing)
class WeOfferViewingTranslation(TranslationOptions):
    fields = ('title', 'selections', 'description' )


@register(Partners)
class PartnersTranslation(TranslationOptions):
    fields = ('title',)

@register(ReadingRating)
class ReadingRatingTranslation(TranslationOptions):
    fields = ('title', 'place', 'description')
    

@register(BooksRating)
class BooksRatingTranslation(TranslationOptions):
    fields = ('title', 'place', 'book', 'author', 'code')


@register(HeaderFooter)
class HeaderFooterTranslation(TranslationOptions):
    fields = (
        'header', 'footer', 'logo', 'name', 'address', 'icons', 'about_library', 'supports', 
        'news', 'services', 'catalog', 'afisha', 'pro_activity', 'page_for_readers', 
        'el_library', 'projects', 'phone_number', 'title_about_library', 'title_afisha', 
        'title_for_readers'
    )
@register(RegisterLogout)
class RegisterLogoutTranslation(TranslationOptions):
    fields = ('title_reg', 'description_reg', 'title_log', 'description_log')
