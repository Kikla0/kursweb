from django.shortcuts import render
from starterdep.settings import WEATHER_API_KEY
from .weather import Weather

def home(request):
    weather = Weather()
    output =  weather.get_input(WEATHER_API_KEY, request.POST['city'], request.POST['date'])
    context = {
        'city': output['city'],
        'date': output['date'],
        'rain': output['rain'],
        'avg': output['avg'],
        'min': output['min'],
        'max': output['max'],
        'hum': output['hum'],
        'wind': output['wind']
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')