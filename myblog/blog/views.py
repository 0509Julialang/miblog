from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import PerfilForm
from .models import Transporte, Alojamiento, Actividades
from blog.forms import TransporteForm, AlojamientoForm, ActividadesForm, BusquedaForm
from .forms import TransporteForm, AlojamientoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def mi_vista_protegida(request):
    # Tu lógica aquí
    pass
 
def home(request):
     return render(request, 'blog/home.html')
 
def about(request):
     return render(request,  'blog/about.html', {'title': 'Acerca de'})

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html')

@login_required
def perfil_view(request):
    perfil = request.user.perfil
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'editar_perfil.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')