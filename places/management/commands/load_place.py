import os

import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned

from places.models import Place, Image


def create_new_place(parsed_place: dict):
    return Place.objects.get_or_create(
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


def save_place_images(place, image_url):
        response = requests.get(image_url)
        response.raise_for_status()

        image_name = os.path.split(image_url)[-1]
        image = ContentFile(response.content, name=image_name)

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
            place, created = create_new_place(parsed_place)
        except MultipleObjectsReturned:
            self.stdout.write(
                self.style.WARNING(
                    'Найдено несколько записей в БД с этим местом'
                )
            )
            return

        if created:
            for image_url in parsed_place['imgs']:
                save_place_images(place, image_url)
                
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
