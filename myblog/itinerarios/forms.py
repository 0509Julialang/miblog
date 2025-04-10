from django import forms
from .models import Itinerario

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }