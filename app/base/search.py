import re
from django.db import connection
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from app.afisha.models import Events
from app.projects.models import MainProjects, AmericanCorner
from app.news.models import DailyNews, EventsNews, BookArrival, MediaCoverage
from app.services.models import Service, ServiceHeader
from app.about_library.models import Management
from app.el_library.models import Book
from app.pro_activity.models import Activity
from app.base.models import ReadingRating, BooksRating

from app.afisha.serializers import EventsSerializer
from app.projects.serializers import MainProjectsSerializer, AmericanCornerSerializer
from app.news.serializers import DailyNewsSerializer, EventsNewsSerializer, BookArrivalSerializer, MediaCoverageSerializer
from app.services.serializers import ServiceSerializer, ServiceHeaderSerializer
from app.about_library.serializer import ManagementSerializer
from app.el_library.serializers import BookSerializer
from app.pro_activity.serializers import ActivitySerializers
from app.base.serializers import ReadingRatingSerializer, BooksRatingSerializer


class GlobalSearch(APIView):

    def get(self, request):
        query = request.query_params.get('search', '').strip()

        if not query or len(query) < 3:
            raise ValidationError({"error": "Введите поисковый запрос (минимум 3 символа)"})

        query = self.clean_query(query)
        query_words = query.split()

        if len(query_words) < 1:
            raise ValidationError({"error": "Запрос слишком короткий, введите хотя бы одно слово"})

        paginator = PageNumberPagination()
        paginator.page_size = int(request.query_params.get('page_size', 10))

        is_postgresql = self.is_postgresql()

        events = self.perform_search(query, query_words, Events, is_postgresql)
        main_projects = self.perform_search(query, query_words, MainProjects, is_postgresql)
        american_corners = self.perform_search(query, query_words, AmericanCorner, is_postgresql)
        daily_news = self.perform_search(query, query_words, DailyNews, is_postgresql)
        events_news = self.perform_search(query, query_words, EventsNews, is_postgresql)
        book_arrival = self.perform_search(query, query_words, BookArrival, is_postgresql)
        media_coverage = self.perform_search(query, query_words, MediaCoverage, is_postgresql)
        service = self.perform_search(query, query_words, Service, is_postgresql)
        service_header = self.perform_search(query, query_words, ServiceHeader, is_postgresql)
        management = self.perform_search(query, query_words, Management, is_postgresql)
        book = self.perform_search(query, query_words, Book, is_postgresql)
        activity = self.perform_search(query, query_words, Activity, is_postgresql)
        reading_rating = self.perform_search(query, query_words, ReadingRating, is_postgresql)
        books_rating = self.perform_search(query, query_words, BooksRating, is_postgresql)
        

        combined_results = list(events) + list(main_projects) + list(american_corners) + list(daily_news) + \
                            list(events_news) + list(book_arrival) + list(media_coverage) + list(service) + \
                            list(service_header) + list(management) + list(book) + list(activity) + list(reading_rating) + list(books_rating)

        if len(combined_results) > 100:
            raise ValidationError({"error": "Результатов слишком много, уточните запрос."})

        combined_results = sorted(combined_results, key=lambda x: self.calculate_relevance(x, query), reverse=True)

        paginated_results = paginator.paginate_queryset(combined_results, request)

        data = []
        for result in paginated_results:
            result_data = {}


            if isinstance(result, Events):
                result_data = EventsSerializer(result).data
                result_data['Pages'] = 'afisha'
            elif isinstance(result, MainProjects):
                result_data = MainProjectsSerializer(result).data
                result_data['Pages'] = 'project'
            elif isinstance(result, AmericanCorner):
                result_data = AmericanCornerSerializer(result).data
                result_data['Pages'] = 'project'
            elif isinstance(result, DailyNews):
                result_data = DailyNewsSerializer(result).data
                result_data['Pages'] = 'news'
            elif isinstance(result, EventsNews):
                result_data = EventsNewsSerializer(result).data
                result_data['Pages'] = 'news'
            elif isinstance(result, BookArrival):
                result_data = BookArrivalSerializer(result).data
                result_data['Pages'] = 'news'
            elif isinstance(result, MediaCoverage):
                result_data = MediaCoverageSerializer(result).data
                result_data['Pages'] = 'news'
            elif isinstance(result, Service):
                result_data = ServiceSerializer(result).data
                result_data['Pages'] = 'services'
            elif isinstance(result, ServiceHeader):
                result_data = ServiceHeaderSerializer(result).data
                result_data['Pages'] = 'services'
            elif isinstance(result, Management):
                result_data = ManagementSerializer(result).data
                result_data['Pages'] = 'about'
            elif isinstance(result, Book):
                result_data = BookSerializer(result).data
                result_data['Pages'] = 'electronic'
            elif isinstance(result, Activity):
                result_data = ActivitySerializers(result).data
                result_data['Pages'] = 'professional'
            elif isinstance(result, ReadingRating):
                result_data = ReadingRatingSerializer(result).data
                result_data['Pages'] = 'main'
            elif isinstance(result, BooksRating):
                result_data = BooksRatingSerializer(result).data
                result_data['Pages'] = 'main'

            data.append(result_data)

        return paginator.get_paginated_response({
            "results": data
        })

    def get_model_search_fields(self, model):
        """
        Возвращает список полей для поиска для данной модели.
        Добавляй свои модели и поля ниже.
        """
        SEARCH_FIELDS = {
            Events: ['title'],
            MainProjects: ['title'],
            AmericanCorner: ['title'],
            DailyNews: ['title'],
            EventsNews: ['title'],
            BookArrival: ['title', 'description', 'author'],
            MediaCoverage: ['title'],
            Service: ['title'],
            ServiceHeader: ['title'],
            Management: ['role', 'full_name'],
            Book: ['title', 'author', 'description'],
            Activity: ['title', 'description'],
            ReadingRating: ['description'],
            BooksRating: ['book', 'author', 'code'],
        }

        model_fields = {f.name for f in model._meta.get_fields()}
        return [field for field in SEARCH_FIELDS.get(model, ['title']) if field in model_fields]

    def perform_search(self, query, query_words, model, is_postgresql):
        filters = Q()
        search_fields = self.get_model_search_fields(model)

        for word in query_words:
            for field in search_fields:
                filters |= Q(**{f"{field}__icontains": word})

        results = model.objects.filter(filters)

        if is_postgresql and 'title' in search_fields:
            results = results.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')

        return results

    def is_postgresql(self):
        return connection.vendor == 'postgresql'


    def calculate_relevance(self, instance, query):
        return sum([1 for word in query.split() if word in getattr(instance, 'title', '')])

    def clean_query(self, query):
        query = re.sub(r'\s+', ' ', query)
        query = re.sub(r'[^\w\s]', '', query)
        return query
class Similars(APIView):
    def get(self, request):
        query = request.query_params.get('search', '').strip()

        if not query:
            raise ValidationError({"error": "Введите поисковый запрос"})

        event_suggestions = self.get_suggestions(query, Events)
        project_suggestions = self.get_suggestions(query, MainProjects)
        corner_suggestions = self.get_suggestions(query, AmericanCorner)
        daily_news_suggestions = self.get_suggestions(query, DailyNews)
        events_news_suggestions = self.get_suggestions(query, EventsNews)
        book_arrival_suggestions = self.get_suggestions(query, BookArrival)
        media_coverage_suggestions = self.get_suggestions(query, MediaCoverage)
        service_suggestions = self.get_suggestions(query, Service)
        service_header_suggestions = self.get_suggestions(query, ServiceHeader)
        management_suggestions = self.get_suggestions(query, Management)
        book_suggestions = self.get_suggestions(query, Book)
        activity_suggestions = self.get_suggestions(query, Activity)
        reading_rating_suggestions = self.get_suggestions(query, ReadingRating)
        books_rating_suggestions = self.get_suggestions(query, BooksRating)

        return Response({
            "afisha": event_suggestions, 
            "projects": project_suggestions,
            "projects": corner_suggestions,
            "news": daily_news_suggestions,
            "news": events_news_suggestions,
            "news": book_arrival_suggestions,
            "news": media_coverage_suggestions,
            "services": service_suggestions,
            "services": service_header_suggestions,
            "about": management_suggestions,
            "electronic": book_suggestions,
            "professional": activity_suggestions,
            "main": reading_rating_suggestions,
            "main": books_rating_suggestions,
        })

    def get_model_search_fields(self, model):
        SEARCH_FIELDS = {
            Events: ['title'],
            MainProjects: ['title'],
            AmericanCorner: ['title'],
            DailyNews: ['title'],
            EventsNews: ['title'],
            BookArrival: ['title', 'description', 'author'],
            MediaCoverage: ['title'],
            Service: ['title'],
            ServiceHeader: ['title'],
            Management: ['role', 'full_name'],
            Book: ['title', 'author', 'description'],
            Activity: ['title', 'description'],
            ReadingRating: ['description'],
            BooksRating: ['book', 'author', 'code'],
        }

        model_fields = {f.name for f in model._meta.get_fields()}
        return [field for field in SEARCH_FIELDS.get(model, ['title']) if field in model_fields]

    def get_suggestions(self, query, model):
        search_fields = self.get_model_search_fields(model)
        filters = Q()

        for field in search_fields:
            filters |= Q(**{f"{field}__icontains": query})

        is_postgresql = self.is_postgresql()
        if is_postgresql and 'title' in search_fields:
            suggestions = model.objects.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')[:10]
        else:
            suggestions = model.objects.filter(filters).distinct()[:10]

        return [
            {
                "id": item.id,
                "title": getattr(item, 'title', str(item))
            }
            for item in suggestions
        ]

    def is_postgresql(self):
        return connection.vendor == 'postgresql'
