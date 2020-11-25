import requests
import datetime
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
            'pais' : r['sys']['country'],
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

    v = 'api.openweathermap.org/data/2.5/forecast/daily?q={},{},{}&cnt={}&appid=3c47737db41fa1aa40de3ad00fb240ec'
    a = v.format(ciudad.nombre)

    full = requests.get(a).json()

    day = datetime.datetime.today()
    fecha_hoy = int(day.strftime('%d'))

    lista_pronostico = {}

    for c in range(0, full['cnt']):
        variable_fecha = full['list'][c]['dt_txt']
        objeto_tiempo = datetime.datetime.strptime(variable_fecha, '%Y-%m-%d %H:%M:%S')

        if int(objeto_tiempo.strftime('%d')) == fecha_hoy or int(objeto_tiempo.strftime('%d')) == fecha_hoy+1:

            if int(objeto_tiempo.strftime('%d')) == fecha_hoy+1:
                today_date += 1
            lista_pronostico[fecha_hoy] = {}
            lista_pronostico[fecha_hoy]['day'] = objeto_tiempo.strftime('%A')
            lista_pronostico[fecha_hoy]['date'] = objeto_tiempo.strftime('%d %b, %Y')
            lista_pronostico[fecha_hoy]['time'] = objeto_tiempo.strftime('%I:%M %p')
            lista_pronostico[fecha_hoy]['FeelsLike'] = full['list'][c]['main']['feels_like']

            lista_pronostico[fecha_hoy]['temperature'] = full['list'][c]['main']['temp']
            lista_pronostico[fecha_hoy]['temperature_max'] = full['list'][c]['main']['temp_max']
            lista_pronostico[fecha_hoy]['temperature_min'] = full['list'][c]['main']['temp_min']

            lista_pronostico[fecha_hoy]['description'] = full['list'][c]['weather'][0]['description']
            lista_pronostico[fecha_hoy]['icon'] = full['list'][c]['weather'][0]['icon']

            fecha_hoy += 1
        else:
            pass
