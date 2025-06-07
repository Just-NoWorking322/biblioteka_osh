from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryMixin, ServiceMixin, ServiceHeaderMixin

router = DefaultRouter()
router.register(r'categories', ServiceCategoryMixin, basename='categories')  # API категорий
router.register(r'services', ServiceMixin, basename='services')  # API услуг
router.register(r'header', ServiceHeaderMixin, basename='header')  # API заголовка

urlpatterns = [
    path('', include(router.urls)),  # Теперь /api/categories/, /api/services/, /api/header/
]
