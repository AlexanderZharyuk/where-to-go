from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=80
    )
    images = models.ImageField(
        verbose_name='Картинка места',
        blank=True,
        null=True
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
        return f'{self.title}'
