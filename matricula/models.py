from django.db import models
from estudiante.models import Estudiante
from curso.models import Curso

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    periodo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, default='matriculado')
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre}"