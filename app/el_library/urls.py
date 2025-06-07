from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.el_library.views import BookViewSet

from app.base.views import PartnersView
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'partner', PartnersView, basename='partner')

# router.register(r'partner', PartnerViewSet, basename='partner')



urlpatterns = [
    path('', include(router.urls)),
]

 