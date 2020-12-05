from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'ciudades'

class Pronostico(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    dia = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    temp_max = models.IntegerField()
    temp_min = models.IntegerField()
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.ciudad.nombre
        
