from datetime import datetime

from django.db import models

NULLABLE = {'blank': True, 'null': True}


def default_datetime():
    return datetime.now()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    body = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    body = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(verbose_name='Дата создания', default=default_datetime)
    change_date = models.DateTimeField(verbose_name='Дата последнего изменения', default=default_datetime)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    title = models.CharField(max_length=100, verbose_name='Название версии')
    feature = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        return f'{self.version_number} ({self.title})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
