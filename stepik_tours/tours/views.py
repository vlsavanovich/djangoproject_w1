from random import seed, randint

from django.http import HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render
from django.views import View

import tours.data as data


class MainView(View):
    def get(self, request):
        seed()
        tours = []
        context = {
            'departures': data.departures,
            'stepik_tours': tours,
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
        }
        while len(tours) != 6:
            index = randint(1, len(data.tours))
            if data.tours[index] not in tours:
                tours.append(data.tours[index])
        return render(request, 'main.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        if departure not in data.departures:
            raise Http404
        tours = []
        price = []
        nights = []
        for i in data.tours:
            tour = data.tours[i]
            if tour['departure'] == departure:
                tours.append(tour)
                price.append(tour['price'])
                nights.append(tour['nights'])
        context = {
            'departures': data.departures,
            'departure': data.departures[departure],
            'stepik_tours': tours,
            'tours_info': {
                'count': len(tours),
                'start_price': min(price),
                'end_price': max(price),
                'start_night': min(nights),
                'end_night': max(nights),
            }
        }

        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in data.tours:
            raise Http404
        tour = data.tours.get(id)
        context = {
            'id': data.tours[id],
            'departures': data.departures,
            'tour': tour,
            'departure': data.departures[tour['departure']],
        }
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('То что Вы искали не может быть найдено... '
                                'ERROR 404')


def custom_handler500(request):
    return HttpResponseServerError('Что=то пошло не так!')
