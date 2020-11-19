from django.core.management.base import BaseCommand
from places.models import Place, Image
import requests
import logging
from io import BytesIO
import hashlib


class Command(BaseCommand):

    def get_url(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response

    def add_arguments(self, parser):
        parser.add_argument('url',
                            type=str,
                            help='Link to .json file to parse')

    def save_place(self, data, place_id):
        place_data = {
            'lon': data.get('coordinates', {}).get('lng', 0),
            'lat': data.get('coordinates', {}).get('lat', 0),
            'title': data.get('title', ''),
            'short_description': data.get('description_short', ''),
            'long_description': data.get('description_long', ''),
            'place_id': place_id
        }
        place, created = Place.objects.get_or_create(**place_data)
        return place

    def save_place_images(self, photos_links, place):
        for link in photos_links:
            img = Image.objects.create(place=place)
            file_content = self.get_url(link).content
            hash_ = hashlib.md5(file_content).hexdigest()
            img.file.save(hash_, BytesIO(file_content))
        return None

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.ERROR)
        raw_data = self.get_url(options['url'])
        data = raw_data.json()
        place = self.save_place(data, hashlib.md5(raw_data.content).hexdigest())
        photos_links = data.get('imgs', [])
        self.save_place_images(photos_links, place)
