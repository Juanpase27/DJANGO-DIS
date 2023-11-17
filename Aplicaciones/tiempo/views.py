from django.shortcuts import render
from .models import tiempo_view

# Create your views here.
def clima(request):
    ciudad = 'Londres'
    response = requests.get(url)
    data = response.json()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

    tiempo = Tiempo(
        city=data['name'],
        temperature=data['main']['temp'],
        wind_speed=data['wind']['speed'],
        latitude=data['coord']['lat'],
        longitude=data['coord']['lon'],
        description=data['weather'][0]['description']
    )


    context = {'tiempo': tiempo}

    return render(request, 'templates/clima.html', context)