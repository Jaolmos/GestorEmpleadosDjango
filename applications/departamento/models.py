from typing import ChainMap
from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    short_name = models.CharField(verbose_name='Nombre corto', max_length=50, unique=True)
    anulate = models.BooleanField(verbose_name='Anulado',default=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']

    def __str__(self):
        return str(self.id) + ' - ' +  self.name + ' - ' + self.short_name 
