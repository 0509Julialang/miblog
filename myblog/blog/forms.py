from django import forms
from blog.models import Transporte, Alojamiento, Actividades
from django.contrib.auth.models import User 
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm

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

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'direccion', 'fecha_nacimiento', 'foto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']