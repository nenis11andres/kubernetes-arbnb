from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Alojamiento, Alquiler
from .forms import AlojamientoForm
from .forms import AlquilerForm
from .forms import ComentarioAlquilerForm



def mis_alojamientos(request):
    alojamientos = Alojamiento.objects.filter(propietario=request.user)
    return render(request, 'mis_alojamientos.html', {'alojamientos': alojamientos})


def editar_alojamiento(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)
    if request.method == 'POST':
        form = AlojamientoForm(request.POST, instance=alojamiento)
        if form.is_valid():
            form.save()
            return redirect('mis_alojamientos')
    else:
        form = AlojamientoForm(instance=alojamiento)
    return render(request, 'editar_alojamiento.html', {'form': form})


def ver_alquileres(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)
    alquileres = Alquiler.objects.filter(alojamiento=alojamiento)
    return render(request, 'ver_alquileres.html', {'alquileres': alquileres})


def nuevo_alojamiento(request):
    if request.method == 'POST':
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.propietario = request.user
            alojamiento.save()
            return redirect('mis_alojamientos')  
    else:
        form = AlojamientoForm()
        
    return render(request, 'nuevo_alojamiento.html', {'form': form})


def mis_alquileres(request):
    alquileres = Alquiler.objects.filter(cliente=request.user)
    return render(request, 'mis_alquileres.html', {'alquileres': alquileres})


from django.contrib.auth.decorators import login_required

def nuevo_alquiler(request):
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alojamiento = form.cleaned_data['alojamiento']
            desde = form.cleaned_data['desde']
            hasta = form.cleaned_data['hasta']
            solapado = Alquiler.objects.filter(
                alojamiento=alojamiento,
                desde__lt=hasta,
                hasta__gt=desde
            ).exists()
            if solapado:
                messages.error(request, "El periodo seleccionado se solapa con otro alquiler.")
            else:
                alquiler = form.save(commit=False)
                alquiler.cliente = request.user
                alquiler.save()
                return redirect('mis_alquileres')
    else:
        form = AlquilerForm()
    return render(request, 'nuevo_alquiler.html', {'form': form})


def comentar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id, cliente=request.user)
    if request.method == 'POST':
        form = ComentarioAlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario guardado correctamente.")
            return redirect('mis_alquileres')
    else:
        form = ComentarioAlquilerForm(instance=alquiler)
    return render(request, 'comentar_alquiler.html', {'form': form, 'alquiler': alquiler})