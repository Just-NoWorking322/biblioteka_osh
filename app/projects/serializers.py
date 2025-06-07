from rest_framework import serializers
from .models import OurProjects, MainProjects, AmericanCorner

class OurProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProjects
        fields = ['id', 'title', 'description', 'image', 'created_at', 'title_2']

class MainProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProjects
        fields = ['id', 'title', 'description', 'image', 'created_at']

class AmericanCornerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmericanCorner
        fields = ['id', 'title', 'description', 'image', 'created_at']