from django.http import HttpResponse
from django.template import loader
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
                'placeId': place.id,
                'detailsUrl': place.detailsUrl
            }
        }
        context['data']['features'].append(feature)

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
