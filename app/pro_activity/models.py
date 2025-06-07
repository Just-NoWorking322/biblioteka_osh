from django.db import models
from ckeditor.fields import RichTextField


class TypeActivity(models.Model):
    type = models.CharField(max_length=155,verbose_name="Тип")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Категорий профессиональная деятельность'
        verbose_name_plural = 'Категорий профессиональная деятельности'

    

class Activity(models.Model):
    title = models.CharField(max_length=255, verbose_name= 'заголовок',unique=True)
    description = RichTextField(verbose_name = 'описание')
    links = models.CharField(max_length=355,verbose_name='Ссылка')
    description_details = RichTextField(verbose_name = "детальное описание")
    type = models.ForeignKey(TypeActivity, verbose_name="category", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'профессиональная деятельность'
        verbose_name_plural = 'профессиональная деятельности'

    def __str__(self):
        return self.title