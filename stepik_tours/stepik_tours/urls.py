from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app_tours.views import DepartureView
from app_tours.views import MainView
from app_tours.views import TourView
from app_tours.views import custom_handler404
from app_tours.views import custom_handler500

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls, name='super_puper'),
    path('departure/<str:departure>/', DepartureView.as_view(), name='departure'),
    path('tour/<int:id>', TourView.as_view(), name='tour'),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = custom_handler404
handler500 = custom_handler500
