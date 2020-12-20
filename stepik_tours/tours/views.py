from django.shortcuts import render
# from django.conf import settings
# from django.views import View
# from stepik_tours import data
from django.http import HttpResponseNotFound


departures = {}
tours = {}


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    departures_title = departures.get(departure)
    return render(request, 'departure.html', context=departures_title)


def tour_view(request, id):
    tour_title = tours.get(id)
    return render(request, 'tour.html', context=tour_title)


def custom_handler404(request, exception):
    return HttpResponseNotFound('То что Вы искали не может быть найдено... '
                                'ERROR 404')
