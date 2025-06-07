from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'afisha', AfishaMixins, basename='afisha')


urlpatterns = [
    path('news/book-arrivals/', EventsListAPIView.as_view(), name='news_book-arrivals_list'),
    path('news/book-arrivals/<int:pk>/', EventsDetailAPIView.as_view(), name='news_book-arrivals_read'),
]

urlpatterns += router.urls
