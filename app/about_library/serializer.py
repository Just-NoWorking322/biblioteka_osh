from rest_framework import serializers
from app.about_library.models import AboutLibrary, TitlesLibrary, Management, StructureAndLibraries, Acts, History

class AboutLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutLibrary
        fields = ['id', 'title_1', 'title_2', 'description', 'image_1', 'image_2', 'image_3']

class TitlesLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TitlesLibrary
        fields = ['id', 'title_1', 'title_2', 'title_3', 'title_4']

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'role', 'full_name', 'image']

class StructureAndLibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructureAndLibraries
        fields = ['id', 'image']

class ActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acts
        fields = ["id", "title", "description", "link"]

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "title", "description", "image"]    