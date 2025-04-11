from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Itinerario
from .forms import ItinerarioForm

def home(request):
    return render(request, 'itinerarios/lista.html')


def lista_itinerarios(request):
    itinerarios = Itinerario.objects.filter(creado_por=request.user)
    return render(request, 'itinerarios/lista.html', {'itinerarios': itinerarios})

def crear_itinerario(request):
    if request.method == 'POST':
        form = ItinerarioForm(request.POST)
        if form.is_valid():
            itinerario = form.save(commit=False)
            itinerario.creado_por = request.user
            itinerario.save()
            return redirect('itinerarios:detalle_itinerario', pk=itinerario.pk)
    else:
        form = ItinerarioForm()
    return render(request, 'itinerarios/formulario.html', {'form': form})


def editar_itinerario(request, pk):
    itinerario = get_object_or_404(Itinerario, pk=pk, creado_por=request.user)
    if request.method == 'POST':
        form = ItinerarioForm(request.POST, instance=itinerario)
        if form.is_valid():
            form.save()
            return redirect('itinerarios:lista')
    else:
        form = ItinerarioForm(instance=itinerario)
    return render(request, 'itinerarios/formulario.html', {'form': form})


def eliminar_itinerario(request, pk):
    itinerario = get_object_or_404(Itinerario, pk=pk, creado_por=request.user)
    if request.method == 'POST':
        itinerario.delete()
        return redirect('itinerarios:lista')
    return render(request, 'itinerarios/confirmar_eliminar.html', {'itinerario': itinerario})

def detalle_itinerario(request, pk):
    itinerario = get_object_or_404(Itinerario, pk=pk)
    return render(request, 'itinerarios/detalle.html', {'itinerario': itinerario})

