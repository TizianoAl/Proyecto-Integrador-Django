from django.contrib import admin
from .models import *

class PronosticoAdmin(admin.ModelAdmin):
    list_display = ('ciudad','dia','fecha','temp_max','temp_min','descripcion')
    list_display_links = ('ciudad','dia','fecha','temp_max','temp_min','descripcion')




admin.site.register(Ciudad)
admin.site.register(Pronostico, PronosticoAdmin)
