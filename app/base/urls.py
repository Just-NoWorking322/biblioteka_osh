from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.base.views import CatalogsViewSet, ElectronicLibraryViewSet, WeOfferViewingView, PartnersView, ReadingRatingView, BooksRatingView, LogoViewsSet, RegisterLogoutView, HeaderFooterView
from app.base.search import GlobalSearch, Similars


router = DefaultRouter()

#Саидахмад
router.register(r'catalogs', CatalogsViewSet, basename='catalogs')
router.register(r'el_library', ElectronicLibraryViewSet, basename='el_Library')

#Алишер 
router.register(r'weofferviewing', WeOfferViewingView, basename='weofferviewing')
router.register(r'partners', PartnersView, basename='partners')
router.register(r'readingrating', ReadingRatingView, basename='readingrating')
router.register(r'booksrating', BooksRatingView, basename='booksrating')
router.register(r'logo', LogoViewsSet, basename='logo')
router.register(r'Register_login', RegisterLogoutView, basename='reg_log')



urlpatterns = [
    path('', include(router.urls)),
    path('search/', GlobalSearch.as_view(), name='global-search'),
    path('similars/', Similars.as_view(), name='similars'),
    path('header-footer/', HeaderFooterView.as_view(), name='header-footer'),
]