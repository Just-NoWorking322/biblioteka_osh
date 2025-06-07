from rest_framework import serializers
from app.pro_activity.models import Activity, TypeActivity


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            "title",
            "description",
            "links",
            'description_details',
            'type',            
        ]

class TypeActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeActivity
        fields = [
            'type', 'id'
        ]