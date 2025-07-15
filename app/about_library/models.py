from django.db import models
from ckeditor.fields import RichTextField

class AboutLibrary(models.Model):
    title_1 = models.CharField(max_length=255, verbose_name="Первый заголовок")
    title_2 = models.CharField(max_length=255, verbose_name="Второй заголовок")
    description = RichTextField(verbose_name="Описание")

    image_1 = models.ImageField(upload_to="First-image/", verbose_name="Первое изображение")
    image_2 = models.ImageField(upload_to="Second-image/", verbose_name="Второе изображение")
    image_3 = models.ImageField(upload_to="Third-image/", verbose_name="Третье изображение")

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = "Страница О библиотеке"
        verbose_name_plural = "Страница О библиотеке"


class TitlesLibrary(models.Model):
    title_1 = models.CharField(max_length=255, verbose_name="Заголовок Руководство")
    title_2 = models.CharField(max_length=255, verbose_name="Заголовок Структура и Библиотеки")
    title_3 = models.CharField(max_length=255, verbose_name="Заголовок Акты Регулирующие деятельность")
    title_4 = models.CharField(max_length=255, verbose_name="Заголовок История")

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = "Заголовок библиотеки"
        verbose_name_plural = "Заголовки библиотек"


class Management(models.Model):
    role = models.CharField(max_length=255, verbose_name="Должность")
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    image = models.ImageField(upload_to="management-image/", verbose_name="Изображение")

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"


class StructureAndLibraries(models.Model):
    image = models.ImageField(upload_to="StructureAndLibraries-image/", verbose_name="Изображение")

    def __str__(self):
        return 'Структура и библиотеки'

    class Meta:
        verbose_name = "Структура и библиотеки"
        verbose_name_plural = "Структуры и библиотеки"
        

class Acts(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    link = models.URLField(
        verbose_name='Сыллка в актах', blank=True, null=True
    )

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Акт, Регулирующие деятельность'
        verbose_name_plural = 'Акты, Регулирующие деятельности'

class History(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='history-image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'