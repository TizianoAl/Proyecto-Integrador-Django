import requests
from django.shortcuts import render
from .models import Ciudad
from .forms import CiudadForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=333079c49b302f10109f0cdea2cedf1a&lang=es'

    if request.method == 'POST':
        form = CiudadForm(request.POST)
        form.save()

    form = CiudadForm()

    ciudades = Ciudad.objects.all()

    clima_data = []

    for ciudad in ciudades:

        r = requests.get(url.format(ciudad)).json()

        clima_ciudad = {
            'ciudad' : ciudad.nombre,
            'temperatura' : r['main']['temp'],
            'descripcion' : r['weather'][0]['description'],
            'icono' : r['weather'][0]['icon'],
        }

        clima_data.append(clima_ciudad)


    context = {'clima_data' : clima_data, 'form' : form}
    return render(request, 'clima/clima.html', context)
