from django.db import models

# Create your models here.
from django.db import models
from rest_framework.permissions import IsAuthenticated

class ServiceCategory(models.Model):
    """Категория услуг (например, Основные услуги, Культурные услуги)."""
    name = models.CharField(
        max_length=255,
        verbose_name="Название категории",
        help_text="Введите название категории услуг (например, Основные услуги, Культурные услуги)."
    )

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        # app_label = 'app.services'  # Явное указание на приложение

    def __str__(self):
        return self.name

class Service(models.Model):
    """Конкретная услуга библиотеки."""
    category = models.ForeignKey(
        ServiceCategory, 
        related_name="services", 
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию, к которой относится эта услуга."
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название услуги",
        help_text="Введите название услуги."
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Описание",
        help_text="Введите описание услуги (необязательно)."
    )
    image = models.ImageField(
        upload_to="services/", 
        blank=True, 
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение, иллюстрирующее услугу (необязательно)."
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

class ServiceHeader(models.Model):
    """Главный заголовок, описание и три изображения."""
    title = models.CharField(
        max_length=255,
        default="НАШИ УСЛУГИ – БОЛЬШЕ, ЧЕМ ПРОСТО КНИГИ",
        verbose_name="Главный заголовок",
        help_text="Введите главный заголовок страницы услуг."
    )
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Описание",
        help_text="Введите описание, которое будет отображаться под заголовком."
    )
    image1 = models.ImageField(
        upload_to="header/", 
        blank=True, 
        null=True,
        verbose_name="Изображение 1",
        help_text="Загрузите первое изображение (слева)."
    )
    image2 = models.ImageField(
        upload_to="header/", 
        blank=True, 
        null=True,
        verbose_name="Изображение 2",
        help_text="Загрузите второе изображение (в центре)."
    )
    image3 = models.ImageField(
        upload_to="header/", 
        blank=True, 
        null=True,
        verbose_name="Изображение 3",
        help_text="Загрузите третье изображение (справа)."
    )

    class Meta:
        verbose_name = "Заголовок страницы"
        verbose_name_plural = "Заголовки страниц"

    def __str__(self):
        return self.title
