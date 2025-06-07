from django.urls import path, include 
from app.page_for_readers.views import BannerViewViewSet, Graphic_workViewViewSet, TitlesViewViewSet, AppointmentViewViewSet, ReadBaseSerializersViewViewSet
from rest_framework.routers import DefaultRouter
from app.base.views import CatalogsViewSet, ElectronicLibraryViewSet
from app.el_library.views import BookViewSet

router = DefaultRouter()
router.register(r'banner', BannerViewViewSet, basename='banner')
router.register(r'graphic_work', Graphic_workViewViewSet, basename='Graphic_work')
router.register(r'titles', TitlesViewViewSet, basename='Titles')
router.register(r'readbase', ReadBaseSerializersViewViewSet, basename='readbase')
router.register(r'appointment', AppointmentViewViewSet, basename='appointment')
router.register(r'catalog', CatalogsViewSet, basename='catalog')
router.register(r'el_Library', ElectronicLibraryViewSet, basename='elLibrary')
router.register(r'el_library', BookViewSet, basename='el_library')

urlpatterns = [

]   

urlpatterns += router.urls
