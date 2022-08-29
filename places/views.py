from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_index_page(request):
    places = Place.objects.all()
    features = [
        {
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
        } for place in places
    ]

    places = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context={'places': places})


def get_place(request, place_id):
    founded_place = get_object_or_404(Place, pk=place_id)
    images_urls = [founded_place.image.url for founded_place
                   in founded_place.images.all()]
    place = {
        'title': founded_place.title,
        'imgs': images_urls,
        'description_short': founded_place.description_short,
        'description_long': founded_place.description_long,
        'coordinates': {
            'lng': founded_place.longitude,
            'lat': founded_place.latitude
        }
    }

    return JsonResponse(
        place,
        json_dumps_params={
            'ensure_ascii': False
        }
    )
