from django.shortcuts import render
from django.http import request
from weatherapp.forms import WeatherForm

# Create your views here.
def WeatherView(request):
    if request.method == 'GET':
        form = WeatherForm()
    else:
        form = WeatherForm(request.POST)
    return render(request, "weather.html", {'form': form})