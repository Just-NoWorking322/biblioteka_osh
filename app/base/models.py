from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Logo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = RichTextField(
        verbose_name="Описание"
    )
    
    image_1 = models.ImageField(upload_to="logo_images/", verbose_name="Изображение первое", blank=True, null=True)
    image_2 = models.ImageField(upload_to="logo_images/", verbose_name="Изображение второе", blank=True, null=True)
    image_3 = models.ImageField(upload_to="logo_images/", verbose_name="Изображение третье", blank=True, null=True)
    image_4 = models.ImageField(upload_to="logo_images/", verbose_name="Изображение чётвёртое", blank=True, null=True)
    image_5 = models.ImageField(upload_to="logo_images/", verbose_name="Изображение пятое", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главные"




class Catalogs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = RichTextField(
        verbose_name="Описание"
    )

    link = models.URLField(
        verbose_name="Ссылка на подробнее",
        blank=True, null=True
    )
    image = models.ImageField(
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Каталоги"
        verbose_name_plural = "Каталоги"

class ElectronicLibrary(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = RichTextField(
        verbose_name="Описание"
    )

    link = models.URLField(
        verbose_name="Ссылка на подробнее",
        blank=True, null=True
    )
    image = models.ImageField(
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Электронная библиотека"
        verbose_name_plural = "Электронные библиотеки"


#Алишер
class WeOfferViewing(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )

    selections = models.CharField(
        max_length=255,
        verbose_name='Подборка для вас'
    )

    description = RichTextField(
        verbose_name='Описание'
    )
    
    video = models.URLField(
         verbose_name='Ссылка на видео', blank=True, null=True
        )
        
    link = models.URLField(
        verbose_name='Ссылка на поподробнее', blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Предлагаем к Просмотру"
        verbose_name_plural = "Предлогают к просмотру"
        
        
class Partners(models.Model): 
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )    
    
    images = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Картинки партнёров'
    )

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class PartnerImage(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name="partner_images")
    image = models.ImageField(upload_to="partners_images/", verbose_name="Изображение")
    links = models.URLField(verbose_name='Ссылка', blank=True, null=True)

    def __str__(self):
        return f"Изображение для {self.partner.title_ru}"

    class Meta:
        verbose_name = "Изображение партнёра"
        verbose_name_plural = "Изображения партнёров"
        
        
class ReadingRating(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Рейтинг читателей(ТОП-3)'
    )

    place = models.CharField(
        max_length=255,
        verbose_name='Место'
    )

    description = RichTextField(
        verbose_name='Имя/Сколько прочитано'
    )

    images = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Фото читателя'
    )


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Рейтинг читателя"
        verbose_name_plural = "Рейтинг читателей"



class BooksRating(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Рейтинг книг(ТОП-3)'
    )
    place = models.CharField(
        max_length=255,
        verbose_name='Место'
    )

    book = models.CharField(
        max_length=255,
        verbose_name='Книга',
        null=True,
        blank=True
    )

    author = models.CharField(
        max_length=255,
        verbose_name='Автор книги',
        null=True,
        blank=True
    )

    code = models.CharField(
        max_length=255,
        verbose_name='Код цивилизации'
    )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Фото книги'
    )


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Рейтинг книги"
        verbose_name_plural = "Рейтинг книг"

    


class HeaderFooter(models.Model):
    header = models.TextField(verbose_name='Хедер')
    footer = models.TextField(verbose_name='Футер')
    logo = models.ImageField(verbose_name='Логотип',upload_to='logo_images/', blank=True, null=True)
    name = models.CharField(verbose_name='Название Библиотеки',max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    icons = models.ImageField(verbose_name='Иконки',upload_to='images/', blank=True, null=True)
    about_library = models.CharField(verbose_name='Страница о библиотеке', max_length=500, blank=True, null=True)
    supports = models.CharField(verbose_name='Поддержать библиотеку', max_length=500, blank=True, null=True)
    news = models.CharField(verbose_name='Новости', max_length=500, blank=True, null=True)
    services = models.CharField(verbose_name='Услуги', max_length=500, blank=True, null=True)
    catalog = models.CharField(verbose_name='Каталог', max_length=500, blank=True, null=True)
    afisha = models.CharField(verbose_name='Афиша', max_length=500, blank=True, null=True)
    pro_activity = models.CharField(verbose_name='Профессиональная деятельность', max_length=500, blank=True, null=True)
    page_for_readers = models.CharField(verbose_name='Читателям', max_length=500, blank=True, null=True)
    el_library = models.CharField(verbose_name='Электронная библиотека', max_length=500, blank=True, null=True)
    projects = models.CharField(verbose_name='Проекты', max_length=500, blank=True, null=True)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=255, blank=True, null=True)
    title_about_library = models.CharField(verbose_name='O библиотеке', max_length=255, blank=True, null=True)
    title_afisha = models.CharField(verbose_name='Мероприятия и деятельность', max_length=255,blank=True, null=True)
    title_for_readers = models.CharField(verbose_name='Читателям', max_length=255,blank=True, null=True)
    instagram_icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)
    facebook_icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)
    google_icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)
    youtube_icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)
    instagram_icon_url = models.URLField(verbose_name='Ссылка Instagram', blank=True, null=True)
    facebook_icon_url = models.URLField(verbose_name='Ссылка Facebook', blank=True, null=True)
    google_icon_url = models.URLField(verbose_name='Ссылка Google', blank=True, null=True)
    youtube_icon_url = models.URLField(verbose_name='Ссылка YouTube', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Заголовок и нижний колонтитул'
        verbose_name_plural = 'Заголовоки и нижние колонтитулы'

    def __str__(self):
        return f"HeaderFooter (id: {self.id})"
    
class RegisterLogout(models.Model):
    title_reg = models.CharField(
        max_length=255,
        verbose_name='Заголовок для регистрации'
        , blank=True, null=True
    )

    description_reg = RichTextField(
        verbose_name="Описание для регистрации"
        , blank=True, null=True
    )

    image_reg = models.ImageField(
        upload_to='register-logo/',
        verbose_name='Изображение для регистрации'
        , blank=True, null=True
    )

    title_log = models.CharField(
        max_length=255,
        verbose_name='Заголовок для выхода'
        , blank=True, null=True
    )

    description_log = RichTextField(
        verbose_name="Описание для выхода"
        , blank=True, null=True
    )


    def __str__(self):
        return self.title_reg
    

    class Meta:
        verbose_name = 'Текст для Регистрации и Входа'
        verbose_name_plural = 'Тексты для Регистрации и Входа'
