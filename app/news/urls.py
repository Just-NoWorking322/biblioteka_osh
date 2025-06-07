from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register(r"news", NewsAPI, basename="news")              # обычные новости
router.register(r"daily-no-pagination", NewsNoApi, basename="dailynoapi")  # новости без пагинации
router.register(r'daily-news', DailyNewsAPI, basename='dailynews')
router.register(r'events-news', EventsNewsAPI, basename='eventsnews')
router.register(r'book-arrivals', BookArrivalAPI, basename='bookarrival')
router.register(r'media-coverage', MediaCoverageAPI, basename='mediacoverage')
router.register(r'catalog', Catalog, basename='catalog')

urlpatterns = [
    path("", include(router.urls)),
]