from django.contrib import admin
from django.urls import path

from .import views

app_name = "departamento_app"


urlpatterns = [
    path('departamento-lista/',views.DepartamentoListView.as_view(), name='departamento-lista'),
    path('nuevo-departamento/',views.NuevoDepartamentoview.as_view(), name='nuevo_departamento'),
]