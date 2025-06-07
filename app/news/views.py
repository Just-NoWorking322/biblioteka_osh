from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from django.http import FileResponse
# from . pagination import NewsPagination
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import Catalog 
from django.db.models import F
from .filters import CatalogFilter  
from rest_framework import mixins, viewsets

# Create your views here.

class NewsAPI(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # pagination_class = NewsPagination  # обычная пагинация

class NewsNoApi(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = DailyNews.objects.all()
    serializer_class = DailyNewsSerializer



    
class DailyNewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = DailyNews.objects.all()
    serializer_class = DailyNewsSerializer


class EventsNewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = EventsNews.objects.all()
    serializer_class = EventsNewsSerializer


class BookArrivalAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = BookArrival.objects.all()
    serializer_class = BookArrivalSerializer

    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk=None):
        book_arrival = self.get_object()
        file_path = book_arrival.file.path
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=book_arrival.file.name)
        return response

    def mark_book_as_read(self, user, book):
        ReadBook.objects.get_or_create(user=user, book=book)
        book.read_count += 1
        book.save()
class MediaCoverageAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = MediaCoverage.objects.all()
    serializer_class = MediaCoverageSerializer
    
class Catalog(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CatalogFilter 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Catalog.objects.filter(pk=instance.pk).update(read_count=F('read_count') + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def increment_read(self, request, pk=None):
        book = self.get_object()
        Catalog.objects.filter(pk=book.pk).update(read_count=F('read_count') + 1)
        book.refresh_from_db()
        return Response({'read_count': book.read_count}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        popular_books = self.get_queryset().order_by('-read_count')[:10]
        serializer = self.get_serializer(popular_books, many=True)
        return Response(serializer.data)

    def mark_book_as_read(self, user, book):
        ReadBook.objects.get_or_create(user=user, book=book)
        book.read_count += 1
        book.save()
