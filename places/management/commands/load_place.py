import os

import requests

from urllib.parse import urlsplit

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned

from places.models import Place, Image


def save_place_images(place, place_images):
    for image_url in place_images:
        response = requests.get(image_url)
        response.raise_for_status()

        image_filepath = os.path.split(image_url)[-1]
        image_filename = urlsplit(image_filepath).path
        image = ContentFile(response.content, name=image_filename)

        Image.objects.create(
            place=place,
            image=image
        )


class Command(BaseCommand):
    help = 'Загружает новое место из json-файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('json_file_url', nargs='?', type=str)

    def handle(self, json_file_url, **options):
        response = requests.get(url=json_file_url)
        response.raise_for_status()

        parsed_place = response.json()
        try:
            place, created = Place.objects.get_or_create(
                title=parsed_place['title'],
                defaults={
                    'description_short': parsed_place.get(
                        'description_short', ''
                    ),
                    'description_long': parsed_place.get(
                        'description_long', ''
                    ),
                    'longitude': parsed_place['coordinates']['lng'],
                    'latitude': parsed_place['coordinates']['lat']
                },
            )
        except MultipleObjectsReturned:
            self.stdout.write(
                self.style.WARNING(
                    'Найдено несколько записей в БД с этим местом'
                )
            )
            return

        if created:
            save_place_images(place, parsed_place['imgs'])

            self.stdout.write(
                self.style.SUCCESS(
                    f'Место {parsed_place["title"]} успешно занесено в БД.'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f'Место {parsed_place["title"]} уже есть в БД.'
                )
            )
