import django_filters
from . models import Catalog

class CatalogFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains', label="Автор")
    title = django_filters.CharFilter(method='filter_by_keywords', label="Название книги") 
    note = django_filters.CharFilter(lookup_expr='icontains', label="Примечание")
    
    class Meta:
        model = Catalog
        fields = ['author', 'title', 'note']  

    def filter_by_keywords(self, queryset, name, value):
        return queryset.filter(title__icontains=value) 
