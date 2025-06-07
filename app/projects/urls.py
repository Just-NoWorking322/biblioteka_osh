from rest_framework.routers import DefaultRouter
from app.projects.views import  OurProjectsViewSet, MainProjectsViewSet, AmericanCornerViewSet

# Роутер для DRF API
router = DefaultRouter()
router.register(r'our-projects', OurProjectsViewSet, basename='our-project')
router.register(r'main-projects', MainProjectsViewSet, basename='main-project')
router.register(r'american-corner', AmericanCornerViewSet, basename='american-corner')

urlpatterns = [
    
]

urlpatterns += router.urls