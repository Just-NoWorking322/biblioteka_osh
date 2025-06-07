from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from app.el_library.serializers import BookSerializer
from app.el_library.models import Book
from app.el_library.filters import BookFilter
from django.db.models import F
from rest_framework import status
    
class BookViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.pk).update(read_count=F('read_count') + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def increment_read(self, request, pk=None):
        book = self.get_object()
        Book.objects.filter(pk=book.pk).update(read_count=F('read_count') + 1)
        book.refresh_from_db()
        return Response({'read_count': book.read_count}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        popular_books = self.get_queryset().order_by('-read_count')[:10]
        serializer = self.get_serializer(popular_books, many=True)
        return Response(serializer.data)
    
    def mark_book_as_read(user, book):
        ReadBook.objects.get_or_create(user=user, book=book)
        book.read_count += 1
        book.save()

# class PartnerViewSet(GenericViewSet, mixins.ListModelMixin):
#     queryset = Partner.objects.all()
#     serializer_class = PartnerSerializer
