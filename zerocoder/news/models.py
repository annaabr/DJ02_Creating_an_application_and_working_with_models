from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description =  models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class News_post_HW(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=100)
    title = models.CharField('Название новости', max_length=50)
    short_description =  models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторизованная новость'
        verbose_name_plural = 'Авторизованные новости'