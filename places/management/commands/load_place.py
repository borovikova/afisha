import os
import requests
import logging

from django.core.management.base import BaseCommand
from io import BytesIO
from urllib.parse import urlparse

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url',
                            type=str,
                            help='Link to .json file to parse')

    def save_place(self, data):
        place_data = {
            'lon': data['coordinates']['lng'],
            'lat': data['coordinates']['lat'],
            'short_description': data['description_short'],
            'long_description': data['description_long'],
        }
        place, created = Place.objects.get_or_create(title=data.get('title', ''), defaults=place_data)
        return place

    def save_place_images(self, photos_links, place):
        for link in photos_links:
            img = Image.objects.create(place=place)
            response = requests.get(link)
            response.raise_for_status()
            file_content = response.content
            img.file.save(os.path.basename(urlparse(link).path), BytesIO(file_content))
        return None

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.ERROR)
        response = requests.get(options['url'])
        response.raise_for_status()
        data = response.json()
        place = self.save_place(data)
        photos_links = data.get('imgs', [])
        self.save_place_images(photos_links, place)
