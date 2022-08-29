from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=80
    )
    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    description_long = HTMLField(
        verbose_name='Подробное описание',
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='Широта',
        validators=[
            MinValueValidator(
                -90,
                message='Широта не может быть меньше -90°'
            ),
            MaxValueValidator(
                90,
                message='Широта не может быть больше 90°'
            )
        ]
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
        validators=[
            MinValueValidator(
                -180,
                message='Долгота не может быть меньше -180°'
            ),
            MaxValueValidator(
                180,
                message='Долгота не может быть больше 180°'
            )
        ]
    )

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        verbose_name_plural = 'Места'
        verbose_name = 'место'


class Image(models.Model):
    place = models.ForeignKey(
        to=Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='places/',
        verbose_name='Картинки места'
    )
    position = models.IntegerField(
        verbose_name='Позиция',
        default=0
    )

    def __str__(self):
        return f'Картинка к {self.place.title}'

    class Meta:
        ordering = ['-position']
