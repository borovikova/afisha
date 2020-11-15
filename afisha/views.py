from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from places.models import Place


def show_map(request):
    template = loader.get_template('index.html')
    context = {'data': {
        'type': 'FeatureCollection',
        'features': []
    }
    }
    places = Place.objects.all()
    for place in places:
        feature = {
            'type': "Feature",
            'geometry': {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            'properties': {
                'title': place.title,
                'place_id': place.id,
                'detailsUrl': reverse('place-detail', args=[place.id])
            }
        }
        context['data']['features'].append(feature)

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        'title': place.title,
        'imgs': [img.file.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lon': place.lat
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
