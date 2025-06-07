from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.about_library.views import AboutLibraryAPI, TitlesLibraryAPI, ManagementAPI, StructureAndLibrariesAPI, ActsAPI, HistoryAPI

router = DefaultRouter()
router.register(r"about-library", AboutLibraryAPI, basename="aboutlibrary")
router.register(r'titles-library', TitlesLibraryAPI, basename='titleslibrary')
router.register(r'management', ManagementAPI, basename='management')
router.register(r'structure-and-libraries', StructureAndLibrariesAPI, basename='structureandlibraries')
router.register(r"acts", ActsAPI, basename="act")
router.register(r'history', HistoryAPI, basename='history')


urlpatterns = [
    path("", include(router.urls)),
]