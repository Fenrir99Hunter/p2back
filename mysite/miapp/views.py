from django.shortcuts import render, redirect, get_object_or_404
from .models import Calificacion
from .forms import CalificacionForm
from django.http import JsonResponse

def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificaciones.html', {'calificaciones': calificaciones})

def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificacion_form.html', {'form': form})

def actualizar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id_calificacion=id_calificacion)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('lista_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificacion_form.html', {'form': form})

def eliminar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id_calificacion=id_calificacion)
    calificacion.delete()
    return redirect('lista_calificaciones')

# API obligatoria (GET)
def api_calificaciones(request):
    data = list(Calificacion.objects.values())
    return JsonResponse(data, safe=False)
