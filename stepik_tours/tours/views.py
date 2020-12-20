from django.shortcuts import render
# from django.conf import settings
# from django.views import View
from django.http import HttpResponseNotFound
from tours import data


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    departures_title = data.departures[departure]
    context = {
        'departure': departures_title
    }
    return render(request, 'departure.html', context=context)


def tour_view(request, id):
    tour_title = data.tours.get(id)
    return render(request, 'tour.html', context=tour_title)


def custom_handler404(request, exception):
    return HttpResponseNotFound('То что Вы искали не может быть найдено... '
                                'ERROR 404')
