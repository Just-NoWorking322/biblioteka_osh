from rest_framework import serializers
from django.conf import settings
from app.el_library.models import Book

class BookSerializer(serializers.ModelSerializer):
    open_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'image', 'link', 'open_url', 'download_url']

    def get_open_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.file.url) if request else obj.file.url

    def get_download_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/v1/el_library/book/{obj.id}/download/') if request else f'/api/v1/el_library/book/{obj.id}/download/'

# class PartnerSerializer(serializers.ModelSerializer):
#     images = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Partner
#         fields = '__all__'
        
#     def get_images(self, obj):
#         request = self.context.get('request')
#         images = obj.partner_images.all()

#         image_urls = []
#         for image in images:
#             if image.image:
#                 image_url = image.image.url
#                 if request:
#                     image_url = request.build_absolute_uri(image_url)
#                 else:
#                     image_url = f"{settings.MEDIA_URL}{image.image}"
#                 image_urls.append(image_url)

#         return image_urls

        






