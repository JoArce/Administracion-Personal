from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    region = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio : {self.calle} {self.no_calle}, {self.comuna} Region {self.region} '

class Empleado(models.Model):
    rut = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f'Empleado {self.id}: Rut {self.rut}, Nombre {self.nombre} {self.apellido} '


