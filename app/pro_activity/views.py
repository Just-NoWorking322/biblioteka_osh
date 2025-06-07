from django.shortcuts import render
from app.pro_activity.serializers import Activity, TypeActivity
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.pro_activity.serializers import ActivitySerializers, TypeActivitySerializers


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class ActivityViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title']
    filterset_fields = ["title"]

class TypeActivityViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = TypeActivity.objects.all()
    serializer_class = TypeActivitySerializers
    