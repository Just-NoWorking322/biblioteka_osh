from .models import User, ReadBook
from .serializers import RegisterSerializer, ReatingsSerializers, PasswordResetConfirmSerializer,SendEmailConfirmationSerializer, CustomTokenObtainPairSerializer,UserCabinetSerializer, ReadBookInputSerializer, ReadBookOutputSerializer
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
#from .serializers import EmailTokenObtainPairSerializer  
from rest_framework.generics import GenericAPIView
from .utils import generate_reset_code, generate_email_code
from django.core.mail import send_mail
from django.conf import settings
from social_core.exceptions import MissingBackend, AuthException
from social_django.utils import load_strategy, load_backend
from app.news.models import BookArrival
from django.utils import timezone
from google.oauth2 import id_token
from google.auth.transport import requests

class CustomTokenObtainPairView(APIView):
    def post(self, request):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class CategoryListView(APIView):
    def get(self, request):
        categories = [
            {"id": choice[0], "name": choice[1]}
            for choice in User.Category.choices
        ]
        return Response(categories)

class UserRegister(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            
            response_data = {
                'user': RegisterSerializer(result['user']).data,
                'tokens': result['tokens']
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncreaseUserRatingView(mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ReatingsSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            user.reitforusers = int(user.reitforusers) + 1
        except:
            user.reitforusers = 1
        user.save()

        serializer = self.get_serializer(user)
        return Response({
            'message': 'Ваш рейтинг обновлён',
            'new_rating': user.reitforusers,
            'user': serializer.data
        })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh токен обязателен."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Вы успешно вышли из аккаунта."}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"detail": "Недействительный токен."}, status=status.HTTP_400_BAD_REQUEST)

class SendEmailConfirmationView(GenericAPIView):
    serializer_class = SendEmailConfirmationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'Пользователь с таким email не найден.'}, status=status.HTTP_404_NOT_FOUND)

            code = generate_email_code(user)

            send_mail(
                subject='Код подтверждения почты',
                message=f'Ваш код подтверждения: {code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

            return Response({'detail': 'Код отправлен на почту.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetCodeView(GenericAPIView):
    serializer_class = SendEmailConfirmationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'Пользователь с таким email не найден.'}, status=status.HTTP_404_NOT_FOUND)

            code = generate_reset_code()
            user.reset_password_code = code
            user.save()

            send_mail(
                subject='Сброс пароля',
                message=f'Ваш код для сброса пароля: {code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

            return Response({'detail': 'Код сброса пароля отправлен на почту.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            new_password = serializer.validated_data['new_password']

            try:
                user = User.objects.get(reset_password_code=code)
            except User.DoesNotExist:
                return Response({'detail': 'Неверный код подтверждения.'}, status=400)

            user.set_password(new_password)
            user.reset_password_code = generate_reset_code()
            user.save()

            return Response({'detail': 'Пароль успешно изменён.'})

        return Response(serializer.errors, status=400)


class UserCabinetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserCabinetSerializer(request.user)
        return Response(serializer.data)
    def patch(self, request):
        serializer = UserCabinetSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    read_only_fields = [
            'id', 'email', 'gender_display', 'category_display',
            'reitforusers', 'is_email_verified', 'read_books', 'read_books_count',
        ]
class ReadBookUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        is_many = isinstance(request.data, list)
        serializer = ReadBookInputSerializer(data=request.data, many=is_many)

        if serializer.is_valid():
            items = serializer.validated_data
            if not is_many:
                items = [items]

            processed_books = []

            for item in items:
                book_id = item['id']
                page = item['page']
                user_email = item['user']

                try:
                    user = User.objects.get(email=user_email)
                except User.DoesNotExist:
                    processed_books.append({
                        'book_id': book_id,
                        'user_email': user_email,
                        'result': 'Пользователь не найден'
                    })
                    continue

                try:
                    book = BookArrival.objects.get(id=book_id)
                except BookArrival.DoesNotExist:
                    processed_books.append({
                        'book_id': book_id,
                        'user_email': user_email,
                        'result': 'Книга не найдена'
                    })
                    continue

                read_book, created = ReadBook.objects.update_or_create(
                    user=user,
                    book=book,
                    defaults={'page': page}
                )

                processed_books.append({
                    'book_id': book_id,
                    'book_title': book.title,
                    'page': page,
                    'user_email': user_email,
                    'result': 'создано' if created else 'обновлено'
                })

            return Response({
                'status': 'success',
                'message': 'Обработка данных завершена',
                'processed_books': processed_books
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'error',
            'message': 'Ошибка в данных',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginAPIView(APIView):
    def post(self, request):
        token = request.data.get('access_token')
        if not token:
            return Response({'error': 'Токен обязателен'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            strategy = load_strategy(request)
            backend = load_backend(strategy=strategy, name='google-oauth2', redirect_uri=None)

            user = backend.do_auth(token)

            if user and user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)

            return Response({'error': 'Ошибка аутентификации'}, status=status.HTTP_401_UNAUTHORIZED)

        except MissingBackend:
            return Response({'error': 'Недопустимый бэкенд'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AuthException as e:
            return Response({'error': f'Ошибка аутентификации через Google: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': f'Неожиданная ошибка: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GoogleIDTokenLoginAPIView(APIView):
    def post(self, request):
        token = request.data.get('id_token')
        if not token:
            return Response({'error': 'ID токен обязателен'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Проверяем и декодируем ID-токен с помощью Google
            idinfo = id_token.verify_oauth2_token(token, requests.Request())

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                return Response({'error': 'Неверный издатель токена'}, status=status.HTTP_401_UNAUTHORIZED)

            email = idinfo.get('email')
            if not email:
                return Response({'error': 'В токене отсутствует email'}, status=status.HTTP_400_BAD_REQUEST)

            user, created = User.objects.get_or_create(email=email)

            # Если пользователь новый — можно заполнить доп. поля
            if created:
                user.full_name = idinfo.get('name', '')
                user.is_email_verified = True
                user.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({'error': f'Неверный ID токен: {str(e)}'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': f'Неожиданная ошибка: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
