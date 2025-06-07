from rest_framework import serializers
from app.page_for_readers.models import Banner, Graphic_work, Titles, ReadBase, Appointment
class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            "title",
            "description",
            "links",
            'image',

        ]
class ReadBaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReadBase
        fields = [
            'title',
            'link'
        ]
class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'title',
            'hosts',
            'schedule'
        ]

class Graphic_workSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graphic_work
        fields = [
            "title",
            "description",
        ]
class TitlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = [
        "work",
        "citizens",
        "hall",
        'readers',
        'books'
        ]