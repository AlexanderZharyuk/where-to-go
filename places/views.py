from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_index_page(request):
    places = Place.objects.all()
    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse(get_place, args=[place.id])
            }
        }
        features.append(feature)

    places = {
        "type": "FeatureCollection",
        "features": features
    }

    data = {'places': places}
    return render(request, 'index.html', context=data)


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images_urls = [founded_place.image.url for founded_place
                   in place.images.all()]
    json_response = {
        'title': place.title,
        'imgs': images_urls,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(
        json_response,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4
        }
    )
