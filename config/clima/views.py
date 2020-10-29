import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=333079c49b302f10109f0cdea2cedf1a&lang=es'
    ciudad = 'London'

    r = requests.get(url.format(ciudad)).json()

    clima_ciudad = {
    'ciudad' : ciudad,
    'temperatura' : r['main']['temp'],
    'descripcion' : r['weather'][0]['description'],
    'icono' : r['weather'][0]['icon'],
    }

    context = {'clima_ciudad' : clima_ciudad}
    return render(request, 'clima/clima.html', context)
