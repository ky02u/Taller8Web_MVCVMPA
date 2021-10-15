from django.http.response import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Ciudad
from .models import tipodocumento
from .models import Persona
from .forms import CiudadForm
from .forms import TipoDocumentoForm
from .forms import PersonaForm

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('RegistroUsuarios/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ciudades(request):
    ciudades = Ciudad.objects.all()
    template = loader.get_template('RegistroUsuarios/ciudades.html')
    context = {'ciudades':ciudades,}
    return HttpResponse(template.render(context,request))

def tipodocumentos(request):
    tipodocumentos = tipodocumento.objects.all()
    template = loader.get_template('RegistroUsuarios/tipodocumentos.html')
    context = {'tipodocumentos':tipodocumentos,}
    return HttpResponse(template.render(context,request))


def new_ciudad(request):

    if request.method == 'POST':
        form = CiudadForm(request.POST)   
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            ciudad = Ciudad(nombre=nombre,descripcion=descripcion)
            ciudad.save()
            return HttpResponseRedirect(reverse('ciudades'))
    else:
        form =  CiudadForm()    
    return render(request, 'RegistroUsuarios/crear_ciudades.html', {'form':form})

def new_tipodocumento(request):

    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)   
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            tipodocumentos = tipodocumento(nombre=nombre,descripcion=descripcion)
            tipodocumentos.save()
            return HttpResponseRedirect(reverse('tipodocumentos'))
    else:
        form =  TipoDocumentoForm()    
    return render(request, 'RegistroUsuarios/crear_tipodocumentos.html', {'form':form})

def personas(request):
    personas = Persona.objects.all()
    template = loader.get_template('RegistroUsuarios/personas.html')
    context = {'personas':personas,}
    return HttpResponse(template.render(context,request))

def new_persona(request):

    if request.method == 'POST':
        form = PersonaForm(request.POST)   
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            idtipodocumento = form.cleaned_data['idtipodocumento']
            documento = form.cleaned_data['documento']
            idlugarresiedencia = form.cleaned_data['idlugarresiedencia']
            fechadenacimiento = form.cleaned_data['fechadenacimiento']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            confirmarcontraseña = form.cleaned_data['confirmarcontraseña']
            lugardenacimiento = form.cleaned_data['lugardenacimiento']                          
            personas = Persona(nombre=nombre,apellido=apellido,idtipodocumento=idtipodocumento,documento=documento,idlugarresidencia=idlugarresidencia,fechadenacimiento=fechadenacimiento,email=email,telefono=telefono,usuario=usuario,contraseña=contraseña,confirmarcontraseña=confirmarcontraseña,lugardenacimiento=lugardenacimiento)
            personas.save()
            return HttpResponseRedirect(reverse('personas'))
    else:
        form =  PersonaForm()    
    return render(request, 'RegistroUsuarios/crear_personas.html', {'form':form})