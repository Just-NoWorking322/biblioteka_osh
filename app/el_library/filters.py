import django_filters
from app.el_library.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label="Название книги")
    author = django_filters.CharFilter(lookup_expr='icontains', label="Автор")
    keywords = django_filters.CharFilter(method='filter_by_keywords', label="Ключевые слова")
    description = django_filters.CharFilter(lookup_expr='icontains', label="Описание")
    
    class Meta:
        model = Book
        fields = ['title', 'author']

    def filter_by_keywords(self, queryset, name, value):
        return queryset.filter(description__icontains=value)