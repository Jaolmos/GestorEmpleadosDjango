from django.contrib import admin
from django.urls import path

from .import views


app_name = "persona_app" #Nombre de todo el conjunto de direcciones

urlpatterns = [
    
    path('',views.InicioView.as_view(),name='inicio'),
    path('lista-empleados-admin/',views.ListaEmpleadosAdmin.as_view(),name='lista_empleados_admin'),
    path('lista-todos-empleados/',views.ListAllEmpleados.as_view(),name='lista_empleados'),
    path('lista-por-area/<short_name>',views.ListByArea.as_view(),name='empleados-area'),
    path('lista-por-trabajo/<short_name>',views.ListByJob.as_view()),
    path('buscar-empleado/',views.ListEmpleadByKw.as_view()),
    path('habilidades-empleado/',views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/',views.EmpleadoDetailView.as_view(),name='detalle-empleado'),
    path('crear-empleado/',views.EmpleadoCreateView.as_view(),name='crear_empleado'),
    path('registro-realizado/',views.SuccessView.as_view(),name='success'),
    path('update-empleado/<pk>/',views.EmpleadoUpdateView.as_view(),name='modificar-empleado'),
    path('eliminar-empleado/<pk>/',views.EmpleadoDeleteView.as_view(),name='eliminar-empleado'),
    path('empleado-eliminado/',views.EmpleadoDeleteView.as_view(),name='eliminado'),
   
    ]