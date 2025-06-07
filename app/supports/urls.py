from rest_framework.routers import DefaultRouter
from .views import LibrarySupportViewSet, LibraryValueViewSet, LibraryTitlesViewSet, PayViewSet

router = DefaultRouter()
router.register(r'library-support', LibrarySupportViewSet, basename='library-support')
router.register(r'library-values', LibraryValueViewSet, basename='library-values')
router.register(r'library-titles', LibraryTitlesViewSet, basename='library-titles')
router.register(r'paytype', PayViewSet, basename='paytype')


urlpatterns = [
    
]

urlpatterns += router.urls
