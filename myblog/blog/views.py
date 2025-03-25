from django.shortcuts import render, redirect
from .blog.models import Transporte, Alojamiento, Actividades
from .blog.forms import TransporteForm, AlojamientoForm, ActividadesForm, BusquedaForm
from .models import Transporte, Alojamiento, Actividades
from .forms import TransporteForm, AlojamientoForm, ActividadesForm, BusquedaForm
 


def home(request):
     return render(request, 'blog/home.html')
 
def agregar_transporte(request):
     if request.method == 'POST':
         form = TransporteForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form = TransporteForm()
     return render(request, 'blog/agregar_transporte.html', {'form': form})
 
def agregar_alojamiento(request):
     if request.method == 'POST':
         form = AlojamientoForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form = AlojamientoForm()
     return render(request, 'blog/agregar_alojamiento.html', {'form': form})
 
def agregar_actividades(request):
     if request.method == 'POST':
         form = ActividadesForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form = ActividadesForm()
     return render(request, 'blog/agregar_actividades.html', {'form': form})
 
def buscar(request):
     if request.method == 'GET':
         form = BusquedaForm(request.GET)
         if form.is_valid():
             query = form.cleaned_data['query']
             resultados = Actividades.objects.filter(nombre__icontains=query)
             return render(request, 'blog/resultados_busqueda.html', {'resultados': resultados})
     else:
         form = BusquedaForm()
     return render(request, 'blog/buscar.html', {'form': form})