from django import forms
from .models import Transporte, Alojamiento, Actividades

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = '__all__'

class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividades
        fields = '__all__'

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)