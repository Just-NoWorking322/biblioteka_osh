from django.db import models
from ckeditor.fields import RichTextField

class Banner(models.Model):
    title = models.CharField(max_length=244, verbose_name='заголовок')
    description = RichTextField(verbose_name= 'описание')
    image = models.ImageField(verbose_name= 'фото')
    links = models.URLField(verbose_name = 'ссылка')

    class Meta:
        verbose_name = 'страница читателям'
        verbose_name_plural = 'страницы читателям'

    def __str__(self):
        return self.title
    
class Graphic_work(models.Model):
    title =  models.CharField(max_length=244, verbose_name='заголовок')
    description = RichTextField(verbose_name= 'описание')

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'

    def __str__(self):
        return self.title
    
class ReadBase(models.Model):
    title = models.CharField(max_length=244, verbose_name="читательные залы")
    link = models.URLField(max_length=244, verbose_name='ссылка', null=True, blank=True)
    class Meta:
        verbose_name = 'Читательный Зал'
        verbose_name_plural = 'Читательные Залы'

    def __str__(self):
        return self.title
        
class Appointment(models.Model):
    title = models.CharField(max_length=244, verbose_name='Название')
    hosts = models.CharField(max_length=244, verbose_name='Принимающие')
    schedule = models.CharField(max_length=244, verbose_name='График приемов')
    class Meta:
        verbose_name = 'График приема'
        verbose_name_plural = 'График приемов'

    def __str__(self):
        return self.title
        
class Titles(models.Model):
    work  = models.CharField(max_length=244, verbose_name='график работы')
    citizens = models.CharField(max_length=244, verbose_name='график приема граждан директора')
    hall =  models.CharField(max_length=244, verbose_name='зал читателей')
    readers =  models.CharField(max_length=244, verbose_name='рейтинг читателей')
    books =  models.CharField(max_length=244, verbose_name='рейтинг книг')

    class Meta:
        verbose_name = 'основные настройки страницы читателя'
        verbose_name_plural = 'основные настройки страницы читателей'

    def __str__(self):
        return self.work
    
