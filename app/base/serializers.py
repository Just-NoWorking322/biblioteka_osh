from rest_framework import serializers
from app.base.models import Logo, Catalogs, WeOfferViewing, Partners, ReadingRating, BooksRating, HeaderFooter, ElectronicLibrary, RegisterLogout
from django.conf import settings


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['id', 'title', 'description', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5']
        

class CatalogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogs
        fields = ['id', 'title', 'description', 'link', 'image']
        
class ElectronicLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicLibrary
        fields = ['id', 'title', 'description', 'link', 'image']
        
class RegisterLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLogout
        fields = ('id', 'title_reg', 'description_reg', 'image_reg', 'title_log', 'description_log')



#Алишер
class WeOfferViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeOfferViewing
        fields = ['id', 'title', 'selections', 'description','video', 'link']

class PartnersSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Partners
        fields = ['id', 'title', 'images', 'links']
        
    def get_images(self, obj):
        request = self.context.get('request')
        image = obj.partner_images.first()  
        if image and image.image:
            return request.build_absolute_uri(image.image.url) if request else f"{settings.MEDIA_URL}{image.image}"
        return None

    def get_links(self, obj):
        link = obj.partner_images.exclude(links__isnull=True).exclude(links__exact='').first()
        if link and link.links:
            return link.links
        return None


class ReadingRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingRating
        fields = ['id', 'title', 'place', 'description', 'images']
        
class BooksRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksRating
        fields = ['id', 'title', 'place', 'book', 'author', 'code', 'image']

        

class HeaderFooterSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)
    icons = serializers.ImageField(required=False)
    instagram_icon = serializers.ImageField(required=False)
    facebook_icon = serializers.ImageField(required=False)
    google_icon = serializers.ImageField(required=False)
    youtube_icon = serializers.ImageField(required=False)

    class Meta:
        model = HeaderFooter
        fields = [
            'id', 
            'header',
            'footer',
            'logo',
            'name',
            'address',
            'icons',
            'about_library',
            'supports',
            'news',
            'services',
            'catalog',
            'afisha',
            'pro_activity',
            'page_for_readers',
            'el_library',
            'projects',
            'phone_number',
            'title_about_library',
            'title_afisha',
            'title_for_readers',
            'instagram_icon',
            'facebook_icon',
            'google_icon',
            'youtube_icon',
            'instagram_icon_url',
            'facebook_icon_url',
            'google_icon_url',
            'youtube_icon_url',
        ]
