from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadAdmin(admin.ModelAdmin): #Para visualizar otros campos en el administrador
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'id',
    )

    search_fields = ('first_name','last_name') #Buscador para filtrar por nombre o y apellidos.
    list_filter = ('departamento','job','habilidades') #Filtro por trabajo
    filter_horizontal = ('habilidades',) #Se filtra entre las habilidades de empleados

admin.site.register(Empleado, EmpleadAdmin)
    