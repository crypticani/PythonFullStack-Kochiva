from django.shortcuts import render
from django.http import request


# Create your views here.
def WeatherView(request):
    return render(request, "weather.html")