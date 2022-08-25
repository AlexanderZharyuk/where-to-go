import os

import requests

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает новое место из json-файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('json_file_url', nargs='?', type=str)

    def handle(self, json_file_url, **options):
        response = requests.get(url=json_file_url)
        response.raise_for_status()

        parsed_place = response.json()
        place, created = Place.objects.get_or_create(
            title=parsed_place['title'],
            defaults={
                'description_short': parsed_place.setdefault(
                    'description_short', ''),
                'description_long': parsed_place.setdefault(
                    'description_long', ''),
                'longitude': parsed_place['coordinates']['lng'],
                'latitude': parsed_place['coordinates']['lat']
            },
        )

        if created:
            for image_url in parsed_place['imgs']:
                response = requests.get(image_url)
                response.raise_for_status()

                image_name = os.path.split(image_url)[-1]
                image = response.content
                prepared_image = ContentFile(image)

                created_image_for_place = Image.objects.create(place=place)
                created_image_for_place.image.save(
                    image_name,
                    prepared_image,
                    save=True
                )

            self.stdout.write(
                self.style.SUCCESS(
                    'Место "%s" успешно занесено в БД.' % parsed_place['title']
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    'Место "%s" уже есть в БД.' % parsed_place['title']
                )
            )