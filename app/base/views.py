from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from app.base.serializers import *
from app.base.models import *
from rest_framework.views import APIView
# Create your views here.


class LogoViewsSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    
class CatalogsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Catalogs.objects.all()
    serializer_class = CatalogsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        data = {
            f"catalog_{item['id']}": item for item in serializer.data
        }
        return Response(data)

class ElectronicLibraryViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = ElectronicLibrary.objects.all()
    serializer_class = ElectronicLibrarySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        data = {
            f"library_{item['id']}": item for item in serializer.data
        }
        return Response(data)


#Алишер
class WeOfferViewingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = WeOfferViewing.objects.all()
    serializer_class = WeOfferViewingSerializer
    

class PartnersView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class ReadingRatingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = ReadingRating.objects.all()
    serializer_class = ReadingRatingSerializer
    

class BooksRatingView(GenericViewSet, 
                         mixins.ListModelMixin):
    queryset = BooksRating.objects.all()
    serializer_class = BooksRatingSerializer

class HeaderFooterView(APIView):
    def get(self, request):
        header_footer = HeaderFooter.objects.last()  
        serializer = HeaderFooterSerializer(header_footer)
        return Response(serializer.data)

class RegisterLogoutView(GenericViewSet, 
                         mixins.ListModelMixin):
    
    queryset = RegisterLogout.objects.all()
    serializer_class = RegisterLogoutSerializer
