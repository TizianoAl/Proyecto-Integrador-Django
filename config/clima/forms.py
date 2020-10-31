from django.forms import ModelForm, TextInput
from .models import Ciudad

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre']
        widgets = {'nombre' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Nombre de la Ciudad'})}
