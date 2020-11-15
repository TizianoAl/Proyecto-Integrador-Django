import requests
from django.shortcuts import render, redirect
from .models import Ciudad
from .forms import CiudadForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=333079c49b302f10109f0cdea2cedf1a&lang=es'

    err_msg = ''
    mensaje = ''
    mensaje_class = ''

    if request.method == 'POST':
        form = CiudadForm(request.POST)

        if form.is_valid():
            nueva_ciudad = form.cleaned_data['nombre']
            existe_ciudad = Ciudad.objects.filter(nombre=nueva_ciudad).count()

            if existe_ciudad == 0:
                r = requests.get(url.format(nueva_ciudad)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'La ciudad que desea ingresar no existe'
            else:
                err_msg = 'La ciudad que desea ingresar ya existe en la base de datos'

        if err_msg:
            mensaje = err_msg
            mensaje_class = 'is-danger'


    form = CiudadForm()

    ciudades = Ciudad.objects.all()

    clima_data = []

    for ciudad in ciudades:

        r = requests.get(url.format(ciudad)).json()

        clima_ciudad = {
            'ciudad' : ciudad.nombre,
            'temperatura' : r['main']['temp'],
            'temp_max' : r['main']['temp_max'],
            'temp_min' : r['main']['temp_min'],
            'humedad' : r['main']['humidity'],
            'descripcion' : r['weather'][0]['description'],
            'icono' : r['weather'][0]['icon'],
        }

        clima_data.append(clima_ciudad)


    context = {
        'clima_data' : clima_data,
        'form' : form,
        'mensaje' : mensaje,
        'mensaje_class' : mensaje_class,
    }
    return render(request, 'clima/clima.html', context)


def eliminar_ciudad(request, nombre_ciudad):
    
    Ciudad.objects.get(nombre=nombre_ciudad).delete()

    return redirect('home')
