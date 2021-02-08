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

    def save_place(self, raw_place):
        place_data = {
            'lon': raw_place['coordinates']['lng'],
            'lat': raw_place['coordinates']['lat'],
            'short_description': raw_place['description_short'],
            'long_description': raw_place['description_long'],
        }
        place, created = Place.objects.get_or_create(
            title=raw_place.get('title', ''), defaults=place_data)
        return place

    def save_place_image(self, link, place):
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
        raw_place = response.json()
        place = self.save_place(raw_place)
        photos_links = raw_place.get('imgs', [])
        for link in photos_links:
            try:
                self.save_place_image(link, place)
            except requests.exceptions.HTTPError:
                print(f"Can't load image {link}")
