from django.shortcuts import render

from django.templatetags.static import static

from .models import Place


def show_index_page(request):
    places = Place.objects.all()
    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.latitude, place.longitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": static('places/moscow_legends.json')
            }
        }
        features.append(feature)

    places = {
        "type": "FeatureCollection",
        "features": features
    }

    data = {'places': places}
    return render(request, 'index.html', context=data)
