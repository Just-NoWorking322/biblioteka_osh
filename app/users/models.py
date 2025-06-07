from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
import re
from django.conf import settings
from app.news.models import BookArrival
from django.core.validators import EmailValidator

class User(AbstractUser):

    class Gender(models.IntegerChoices):
        MALE = 1, 'Мужской'
        FEMALE = 2, 'Женский'

    class Category(models.IntegerChoices):
        STUDENT = 1, 'Студент'
        SCHOOLBOY = 2, 'Школьник'
        PENSIONER = 3, 'Пенсионер'
        EMPLOYEE = 4, 'Служащий'
        SEN = 5, 'ОВЗ, ограниченные возможности здоровья'
        OTHER = 6, 'Другое'

    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )

    gender = models.IntegerField(
        choices=Gender.choices,
        null=True,
        blank=True,
        default=Gender.MALE,
        verbose_name="Пол"
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения"
    )

    category = models.IntegerField(
        choices=Category.choices,
        null=True, blank=True,
        default=Category.OTHER,
        verbose_name="Категория"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )

    def validate_phone_number(value):
        pattern = r'^\+996\d{9}$'
        if not re.match(pattern, value):
            raise ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")

    phone = models.CharField(
        max_length=20,
        unique=True,
        #validators=[validate_phone_number],
        null=True, blank=True,
        verbose_name="Номер телефона"
    )

    reitforusers = models.PositiveIntegerField(
        default=0,
        verbose_name="Рейтинг пользователя"
    )
    is_email_verified = models.BooleanField(default=False, verbose_name="Email подтвержден")
    reset_password_code = models.CharField(max_length=6, blank=True, null=True)
    avatarka = models.ImageField(upload_to="avatarka/", verbose_name="Изображение Профиля", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.full_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
    

class ReadBook(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='read_books'
    )
    book = models.ForeignKey(BookArrival, on_delete=models.CASCADE, blank=True, null=True)
    page = models.PositiveIntegerField()
    
    
    file = models.FileField(upload_to='readbooks/files/', blank=True, null=True, verbose_name='Файл для скачивания')
    image = models.ImageField(upload_to='readbooks/images/', blank=True, null=True, verbose_name='Изображение')
    
    def __str__(self):
        return f"{self.user.email} read {self.book} (page {self.page})"
