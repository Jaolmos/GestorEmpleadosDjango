from django.shortcuts import render
from django.views.generic.edit import FormView
from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm
from django.views.generic import ListView


class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/departamento-lista.html'
    context_object_name = 'departamentos'


class NuevoDepartamentoview(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form): 
        print('*********Estamos en el formvalid')
        
        depart = Departamento(  #Se crea una instancia de modelo departamento
            name = form.cleaned_data['departamento'], #departamento de forms, de la clase NewDepartamentforms
            short_name = form.cleaned_data['nombre_corto'],
        )
        depart.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depart
        )
        return super(NuevoDepartamentoview,self).form_valid(form)
        
         



        
