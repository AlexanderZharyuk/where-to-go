from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=80
    )
    description_short = models.TextField(
        verbose_name='Короткое описание'
    )
    description_long = models.TextField(
        verbose_name='Подробное описание'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )

    def __str__(self):
        return f'{self.id}. {self.title}'


class Image(models.Model):
    place = models.ForeignKey(
        to=Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    images = models.ImageField(
        upload_to='media/',
        verbose_name='Картинки места'
    )
    is_main = models.BooleanField(
        verbose_name='Главная фотография места',
        default=False
    )

    def __str__(self):
        return f'Картинка к {self.place.title}'
