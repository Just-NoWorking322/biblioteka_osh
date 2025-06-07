from django.db import models
from ckeditor.fields import RichTextField


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название книги"
    )
    author = models.CharField(
        max_length=255,
        verbose_name="Автор"
    )
    description = RichTextField(
        verbose_name="Описание",
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='book_images/',
        verbose_name="Изображение книги",
        blank=True, null=True
    )
    file = models.FileField(
        upload_to='books/files/',
        verbose_name="Файл книги",
        blank=True, null=True
    )
    link = models.URLField(verbose_name="Ссылка", blank=True, null=True)

    read_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


# class Partner(models.Model): 
#     title = models.CharField(
#         max_length=255,
#         verbose_name='Заголовок'
#     )    

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Партнёр и Поддержка"
#         verbose_name_plural = "Партнёры и Поддержки"


# class PartnerImage(models.Model):
#     partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name="partner_images")
#     image = models.ImageField(upload_to="partners_images/", verbose_name="Изображение")


#     def __str__(self):
#         return f"Изображение для {self.partner.title}"

#     class Meta:
#         verbose_name = "Изображение партнёра и"
#         verbose_name_plural = "Изображения партнёров и"
