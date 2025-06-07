from rest_framework import mixins, viewsets
from .models import LibrarySupport, LibraryValue, LibraryTitles, Pay
from .serializers import LibrarySupportSerializer, LibraryValueSerializer, LibraryTitlesSerializer, PaySerializers

class LibrarySupportViewSet(mixins.ListModelMixin, 
                            viewsets.GenericViewSet):
    queryset = LibrarySupport.objects.all()
    serializer_class = LibrarySupportSerializer


class LibraryValueViewSet(mixins.ListModelMixin, 
                          viewsets.GenericViewSet):
    queryset = LibraryValue.objects.all()
    serializer_class = LibraryValueSerializer

class LibraryTitlesViewSet(mixins.ListModelMixin, 
                          viewsets.GenericViewSet):
    queryset = LibraryTitles.objects.all()
    serializer_class = LibraryTitlesSerializer

class PayViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializers