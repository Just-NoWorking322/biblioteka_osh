from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from .models import OurProjects, MainProjects, AmericanCorner
from .serializers import OurProjectsSerializer, MainProjectsSerializer, AmericanCornerSerializer
from django.shortcuts import render
from rest_framework import mixins

class OurProjectsViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = OurProjects.objects.all()
    serializer_class = OurProjectsSerializer

class MainProjectsViewSet(ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = MainProjects.objects.all()
    serializer_class = MainProjectsSerializer

class AmericanCornerViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = AmericanCorner.objects.all()
    serializer_class = AmericanCornerSerializer
