from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from ..models import Ciudad
from ..forms import CiudadForm

def obtener_ciudades(request):
    ciudades = Ciudad.objects.all()
    template = loader.get_template('ciudades/ciudades.html')
    context = {
        'ciudades': ciudades
    }
    return HttpResponse(template.render(context, request))

def crear_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            ciudad = Ciudad(nombre=nombre, descripcion=descripcion)
            ciudad.save()
    else:
        form = CiudadForm()
        return render(request, 'forms/form_template.html', {'form': form})
    return HttpResponseRedirect(reverse('obtener_ciudades'))

def actualizar_ciudad(request, id):
    ciudad = Ciudad.objects.get(id=id)
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            ciudad.nombre = form.cleaned_data['nombre']
            ciudad.descripcion = form.cleaned_data['descripcion']
            ciudad.save()
    else:
        form = CiudadForm(data={'nombre': ciudad.nombre, 'descripcion': ciudad.descripcion})
        return render(request, 'forms/form_template.html', {'form': form})     
    return HttpResponseRedirect(reverse('obtener_ciudades')) 

def eliminar_ciudad(request, id):
    if request.method == 'POST':
        ciudad = Ciudad.objects.get(id=id)
        ciudad.delete()
        return HttpResponse(HttpResponse.status_code)
