from django.contrib import admin
from .models import Carrera

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'duracion', 'modalidad', 'activa')
    search_fields = ('nombre', 'codigo')
    list_filter = ('activa', 'modalidad')