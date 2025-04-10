from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Perfil
from .forms import PerfilForm
from .forms import RegistroForm
from .models import Transporte, Alojamiento, Actividades
from blog.forms import TransporteForm, AlojamientoForm, ActividadesForm, BusquedaForm
from .forms import TransporteForm, AlojamientoForm
from django.contrib.auth.decorators import login_required

@login_required
def mi_vista_protegida(request):
    # Tu lógica aquí
    pass
 
def home(request):
     return render(request, 'blog/base.html')
 
def about(request):
     return render(request,  'blog/about.html', {'title': 'Acerca de'})

@login_required
def agregar_transporte(request):
    if request.method == 'POST':
        form = TransporteForm(request.POST)
        if form.is_valid():
            transporte = form.save(commit=False)
            transporte.usuario = request.user
            transporte.save()
            return redirect('home')
    else:
        form = TransporteForm()
    return render(request, 'blog/agregar_transporte.html', {'form': form})
 
@login_required
def agregar_alojamiento(request):
    if request.method == 'POST':
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.usuario = request.user
            alojamiento.save()
            return redirect('home')
    else:
        form = AlojamientoForm()
    return render(request, 'blog/agregar_alojamiento.html', {'form': form})
 
@login_required
def agregar_actividades(request):
    if request.method == 'POST':
        form = ActividadesForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.usuario = request.user
            actividad.save()
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
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def perfil(request):
    return render(request, 'blog/perfil.html')
     

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('detalle_perfil')
        else:
            print(form.errors)
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'blog/editar_perfil.html', {'form': form})

@login_required
def detalle_perfil(request):
    perfil = request.user.perfil
    return render(request, 'blog/detalle_perfil.html', {'perfil': perfil})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def perfil_view(request):
    if not hasattr(request.user, 'perfil'):
        Perfil.objects.create(user=request.user)
    perfil = request.user.perfil
    return render(request, 'blog/perfil.html', {'perfil': perfil})

def itinerarios_view(request):
    return render(request, 'blog/itinerarios.html')

def lista_itinerarios(request):
    # lógica para mostrar itinerarios
    return render(request, 'blog/lista_itinerarios.html')