

# Create your views here.
from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import Service, ServiceCategory, ServiceHeader
from .serializers import ServiceSerializer, ServiceCategorySerializer, ServiceHeaderSerializer

class ServiceMixin(GenericViewSet, mixins.ListModelMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class ServiceCategoryMixin(GenericViewSet, mixins.ListModelMixin):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
class ServiceHeaderMixin(GenericViewSet, mixins.ListModelMixin):
    queryset = ServiceHeader.objects.all()
    serializer_class = ServiceHeaderSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)