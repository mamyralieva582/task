from django.db import models

class Clothes(models.Model):
    author = models.CharField(max_length=10, verbose_name='Названия')
    description = models.TextField(max_length=50, blank=True, verbose_name='Описание')
    title = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='posts_img', blank=True, verbose_name='Фото')


def __str__(self):
    return self.title 

    
