from django.shortcuts import render
from app.page_for_readers.models import Banner, Graphic_work, Titles, Appointment, ReadBase
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.page_for_readers.serializers import BannerSerializers, Graphic_workSerializers, TitlesSerializers, AppointmentSerializers, ReadBaseSerializers
from rest_framework.mixins import RetrieveModelMixin
# Create your views here.

class BannerViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers

class Graphic_workViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Graphic_work.objects.all()
    serializer_class = Graphic_workSerializers

class AppointmentViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    
class ReadBaseSerializersViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = ReadBase.objects.all()
    serializer_class = ReadBaseSerializers

class TitlesViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializers
