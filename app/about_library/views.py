from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from app.about_library.models import *
from app.about_library.serializer import *

class AboutLibraryAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = AboutLibrary.objects.all()
    serializer_class = AboutLibrarySerializer
    
class TitlesLibraryAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = TitlesLibrary.objects.all()
    serializer_class = TitlesLibrarySerializer

class ManagementAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    
class StructureAndLibrariesAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = StructureAndLibraries.objects.all()
    serializer_class = StructureAndLibrariesSerializer
    
    
class ActsAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Acts.objects.all()
    serializer_class = ActsSerializer

class HistoryAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = History.objects.all()
    serializer_class = HistorySerializer