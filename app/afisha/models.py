from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Afisha(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', help_text='Объявление о мероприятиях')
    image = models.ImageField(verbose_name='Изображение', upload_to='afisha/',  blank=True, null=True)
    description = RichTextField(verbose_name='Описание', help_text='Описание библиотеки')

    title_2 = models.CharField(max_length=255, verbose_name='Заголовок о мероприятиях')

    class Meta:
        verbose_name = "Объявление о мероприятиях"
        verbose_name_plural = "Объявления о мероприятиях"


class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', help_text='Объявление о мероприятиях')
    description = RichTextField(verbose_name='Описание мероприятия')
    image = models.ImageField(verbose_name='Изображение к мероприятию', upload_to='afisha/',  blank=True, null=True)
    information = RichTextField(verbose_name='Общая информация', blank=True, null=True)
    link =models.URLField(verbose_name='Ссылка на "подробнее', blank=True, null=True)
    
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
