from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from ..models import Persona
from ..forms import PersonaForm


def obtener_personas(request):
    personas = Persona.objects.all()
    template = loader.get_template('personas/personas.html')
    context = {
        'personas': personas
    }
    return HttpResponse(template.render(context, request))


def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombres']
            apellido = form.cleaned_data['apellidos']
            tipo_documento = form.cleaned_data['tipo_documento']
            numero_documento = form.cleaned_data['numero_documento']
            lugar_residencia = form.cleaned_data['lugar_residencia']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            persona = Persona(nombres=nombre, apellidos=apellido, tipo_documento=tipo_documento,
                              numero_documento=numero_documento,  lugar_residencia=lugar_residencia,
                              fecha_nacimiento=fecha_nacimiento, email=email, telefono=telefono,
                              usuario=usuario, password=password)
            persona.save()
    else:
        form = PersonaForm()
        return render(request, 'forms/form_template.html', {'form': form})
    return HttpResponseRedirect(reverse('obtener_personas'))


def actualizar_persona(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona.nombres = form.cleaned_data['nombres']
            persona.apellidos = form.cleaned_data['apellidos']
            persona.tipo_documento = form.cleaned_data['tipo_documento']
            persona.numero_documento = form.cleaned_data['numero_documento']
            persona.lugar_residencia = form.cleaned_data['lugar_residencia']
            persona.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            persona.email = form.cleaned_data['email']
            persona.telefono = form.cleaned_data['telefono']
            persona.usuario = form.cleaned_data['usuario']
            persona.password = form.cleaned_data['password']
            persona.save()
    else:
        form = PersonaForm(data={'nombres': persona.nombres, 'apellidos': persona.apellidos, 'tipo_documento': persona.tipo_documento,
                                 'numero_documento': persona.numero_documento, 'lugar_residencia': persona.lugar_residencia,
                                 'fecha_nacimiento': persona.fecha_nacimiento, 'email': persona.email, 'telefono': persona.telefono,
                                 'usuario': persona.usuario})
        return render(request, 'forms/form_template.html', {'form': form})
    return HttpResponseRedirect(reverse('obtener_personas'))

def eliminar_persona(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
        persona.delete()
    return HttpResponseRedirect(reverse('obtener_personas'))
