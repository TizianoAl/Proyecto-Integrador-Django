# Klima

## Descripción:

Página meteorológica en el cual el usuario inserta una ciudad en el buscador y le
devuelve el nombre de la ciudad que ingreso, la temperatura en °C, la temperatura máxima en °C, la temperatura mínima en °C, la humedad, la descripción del clima y una imagen
de la descripción.
Si desea ver el pronostico extendido de la ciudad que ingresó, debe clickear el nombre de la ciudad y podrá ver un pronostico extendido de 4 días, que mostrará el día, la fecha, la temperatura máxima en °C, la temperatura mínima en °C, la descripción del clima y una imagen de la descripción.
Después una vez ingresada la ciudad el usuario puede eliminar la ciudad que ingreso.

## Requerimientos para correr el programa:

  - asgiref==3.2.10
  - certifi==2020.6.20
  - chardet==3.0.4
  - Django==3.1.2
  - idna==2.10
  - pytz==2020.1
  - requests==2.24.0
  - sqlparse==0.4.1
  - urllib3==1.25.11

Una vez estando en el Virtual Environment, ejecutar el siguiente comando en la terminal:

```sh
$ pip install -r requirements.txt
```

## Instalación:

Deberá descargar los archivos desde el repositorio del proyecto con los siguiente comandos:

```sh
$ git init
$ git clone --branch master https://github.com/TizianoAl/Proyecto-Integrador-Django.git
```

## Ejecución del Proyecto:

Para ejecutar proyecto deberá ejecutar el siguiente comando en la ruta donde se encuentre el archivo manage.py:

```sh
$ python manage.py runserver
```

## Uso de la página:

Una vez que le usuario haya instalado y ejecutado el programa, va a poder ingresar una o varias ciudades
del cual quiera saber el clima y si lo desea va a poder eliminar la ciudad que ingreso.
