from django.db.models import query
from applications.departamento.models import Departamento
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Empleado 

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )

class InicioView(TemplateView): #Vista que carga la pagina home    
    template_name = 'home.html'


class ListAllEmpleados(ListView): #ListAllEmpleados trabaja con la lista generica ListView
    template_name = 'persona/list_all.html'
    context_object_name = 'lista_empleados'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("keyword", '')  
        lista_trabajo = Empleado.objects.filter(
            full_name__icontains = palabra_clave #Arreglar para que busque con full_name
        )
        return lista_trabajo


class ListaEmpleadosAdmin(ListView): 
    template_name = 'persona/lista-empleado-admin.html'
    context_object_name = 'lista_empleadoss'
    paginate_by = 5
    model = Empleado

class ListByArea(ListView): #ListAllEmpleados trabaja con la lista generica ListView
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleadoss'

    def get_queryset(self):
        area = self.kwargs['short_name'] #Indicamos que parametro de url queremos recoger
        lista_areas= Empleado.objects.filter(  
        departamento__short_name = area 
        ) 
        return lista_areas

#3 Listar los empleados pos trabajo*******PENDIENTE DE TERMINAR*********
class ListByJob(ListView):
    template_name = 'persona/list_by_job.html' 

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista_trabajo = Empleado.objects.filter(
        job = trabajo     
        )
        return lista_trabajo


class ListEmpleadByKw(ListView):
    template_name = 'persona/by_keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("keyword",)  #peticion GET que nos trae la id keyword del formulario
        lista_trabajo = Empleado.objects.filter( #Filtra por palabra clave para retornar lista
        first_name = palabra_clave   
        )
        return lista_trabajo
       

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'skills'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=6) #Recuperarmos al empleado por un dato especifico
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detalle_empleado.html'
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = [#Campos que queremos que se vean en formulario crear cliente
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:lista_empleados') #pagina de destino
    
    #Arreglar
    def form_valid(self, form): #Este metodo se realiza cuando se han espeficigado todos los campos del formulario
        empleado = form.save(commit=False) #Se recupera una instancia del formulario.Se guarda directamente en la bd
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:lista_empleados_admin') #pagina de destino
 

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:lista_empleados_admin')





