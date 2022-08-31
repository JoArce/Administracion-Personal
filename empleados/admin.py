from django.contrib import admin

# Register your models here.
from empleados.models import Empleado, Domicilio

admin.site.register(Empleado)
admin.site.register(Domicilio)