from app.afisha.models import *
from app.afisha.serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets


class EventsListAPIView(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class EventsDetailAPIView(RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class AfishaMixins(GenericViewSet,
                    mixins.ListModelMixin):
   
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer
    
