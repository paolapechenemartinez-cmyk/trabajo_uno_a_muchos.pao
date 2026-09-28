from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)   # ← Cambiado
    descripcion = models.TextField(max_length=500)
    intensidad_horaria = models.IntegerField()
    nivel = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre