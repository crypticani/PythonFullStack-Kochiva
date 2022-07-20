from django.urls import path
from weatherapp.views import WeatherView

urlpatterns = [
    path('weather/', WeatherView, name="weather" )
]