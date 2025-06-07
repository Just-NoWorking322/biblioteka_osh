from rest_framework import serializers
from .models import Events, Afisha

class AfishaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afisha
        fields = ['id', 'title', 'image', 'description', 'title_2']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'information', 'title', 'description', 'image', 'link']