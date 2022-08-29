from django.db import models

# Create your models here.

class Empleado(models.Model):
    rut = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)


