from django.urls import path, include 
from app.pro_activity.views import ActivityViewViewSet, TypeActivityViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'activity', ActivityViewViewSet, basename='activity')
router.register(r'type_activity', TypeActivityViewSet, basename='typeactivityViewSet')

urlpatterns = [

]

urlpatterns += router.urls
