from rest_framework import serializers
from .models import User, ReadBook
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Неверный email или пароль'})

        if not user.check_password(password):
            raise serializers.ValidationError({'detail': 'Неверный email или пароль'})

        if not user.is_active:
            raise serializers.ValidationError({'detail': 'Пользователь неактивен'})

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'email': user.email,
            'user_id': user.id,
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'gender', 'birth_date', 'category', 'email', 'phone', 'read_books')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    gender_display = serializers.SerializerMethodField(read_only=True)
    category_display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'full_name', 'gender', 'gender_display',
            'birth_date', 'category', 'category_display',
            'email', 'phone', 'password', 'password2'
        )

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_category_display(self, obj):
        return obj.get_category_display()

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            full_name=validated_data['full_name'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date'],
            category=validated_data['category'],
            email=validated_data['email'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return {
            'user': user,
            'tokens': tokens
        } 


class ReatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'reitforusers')

class SendEmailConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class PasswordResetConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True, min_length=8)





class ReadBookInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()  
    title = serializers.CharField(max_length=255, required=False) 
    page = serializers.IntegerField()
    user = serializers.EmailField()
    
    file = serializers.FileField(required=False, allow_null=True)
    image = serializers.ImageField(required=False, allow_null=True)
    
class ReadBookOutputSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    # Достаем из BookArrival
    download_url = serializers.SerializerMethodField()
    open_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ReadBook
        fields = [
            'book_title', 'book_author', 'page', 'user_email',
            'download_url', 'open_url', 'image_url'
        ]

    def get_download_url(self, obj):
        request = self.context.get('request')
        if obj.book and obj.book.file:
            return request.build_absolute_uri(f'/api/v1/news/book-arrivals/{obj.book.id}/download/') if request else f'/api/v1/news/book-arrivals/{obj.book.id}/download/'
        return None

    def get_open_url(self, obj):
        request = self.context.get('request')
        if obj.book and obj.book.file:
            return request.build_absolute_uri(obj.book.file.url) if request else obj.book.file.url
        return None

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.book and obj.book.image:
            return request.build_absolute_uri(obj.book.image.url) if request else obj.book.image.url
        return None
class UserCabinetSerializer(serializers.ModelSerializer):
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    read_books = ReadBookOutputSerializer(many=True, read_only=True)
    read_books_count = serializers.SerializerMethodField()
    avatarka = serializers.FileField(required=False, allow_null=True, write_only=True)
    avatarka_url = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = User
        fields = [
            'id', 'full_name', 'email', 'phone', 'gender', 'gender_display',
            'birth_date', 'category', 'category_display', 'reitforusers',
            'is_email_verified', 'read_books', 'read_books_count',
            'avatarka', 'avatarka_url'
        ]
        read_only_fields = [
            'id', 'email', 'gender_display', 'category_display',
            'reitforusers', 'is_email_verified', 'read_books', 'read_books_count'
        ]

    def get_read_books_count(self, obj):
        return obj.read_books.count()

    def get_avatarka_url(self, obj):
        request = self.context.get('request')
        if obj.avatarka and hasattr(obj.avatarka, 'url') and request:
            return request.build_absolute_uri(obj.avatarka.url)
        return None
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        if not instance.avatarka:
            rep['avatarka'] = None

        return rep
