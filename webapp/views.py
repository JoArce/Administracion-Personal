from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from empleados.models import Empleado, Domicilio


def bienvenido(request):
     no_personas = Empleado.objects.count()
     return render(request, 'bienvenida.html', {'no_personas':no_personas})