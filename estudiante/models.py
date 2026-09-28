from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    documento = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"