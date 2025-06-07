from rest_framework import serializers
from .models import Service, ServiceCategory, ServiceHeader

class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для отдельных услуг."""
    class Meta:
        model = Service
        fields = ["id", "title", "description", "image", 'category']

class ServiceCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий, включая вложенные услуги."""
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ["id", "name", "services"]

class ServiceHeaderSerializer(serializers.ModelSerializer):
    """Сериализатор для заголовка, описания и изображений."""
    class Meta:
        model = ServiceHeader
        fields = ['title', 'description', 'image1', 'image2', 'image3']
