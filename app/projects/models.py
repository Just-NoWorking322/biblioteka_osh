from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone 

class OurProjects(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта (Кыргызский)")
    image = models.ImageField(upload_to='our_projects/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    title_2 = models.CharField(max_length=255, verbose_name="основыные проекты")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наш проект"
        verbose_name_plural = "Наши проекты"

class MainProjects(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название основного проекта")
    description = RichTextField(verbose_name="Описание основного проекта")
    image = models.ImageField(upload_to='main_projects/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Основной проект"
        verbose_name_plural = "Основные проекты"

class AmericanCorner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='american_corner/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Американский уголок"
        verbose_name_plural = "Американские уголки"
