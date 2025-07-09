from django.db import models
from ckeditor.fields import RichTextField


class LibrarySupport(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to='library-support/',verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поддержка библиотеки'
        verbose_name_plural = 'Поддержка библиотеки'

class LibraryValue(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок ценности')
    icon = models.ImageField(upload_to='library-values/icons/', verbose_name='Иконка')
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = RichTextField(verbose_name='Полное описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ценность библиотеки'
        verbose_name_plural = 'Ценности библиотеки'
    
class LibraryTitles(models.Model):
    title_1 = models.CharField(max_length=255, verbose_name="Ценности библиотеки")
    title_2 = models.CharField(max_length=255, verbose_name="Наши партнеры")
    title_3 = models.CharField(max_length=255, verbose_name="Способ оплаты")
    left_description = RichTextField(verbose_name='Оплата наличными')
    right_description = RichTextField(verbose_name='Оплата перевод')

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Заголовки'
        verbose_name_plural = 'Заголовки'

class Pay(models.Model):
    title = models.CharField(max_length=255, verbose_name="Номер телефона")
    image_logo = models.ImageField(upload_to='pay/', verbose_name='Логотип')
    image_qr = models.ImageField(upload_to='qr/', verbose_name='Qr') 
    links = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплат'
        verbose_name_plural = 'Способы оплаты'
    