from django.db import models
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField(verbose_name='Habilidad', max_length=100)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'
        
    def __str__(self):
            return str(self.id) + ' - ' +  self.habilidad    
      


class Empleado(models.Model): #Modelo para tabla 'Empleado'
    
    JOB_CHOICES = (
        ('1', 'Informatico'),
        ('2', 'Administrador'),
        ('3', 'Economista'),
        ('4', 'Otro'),
    )
    
    first_name = models.CharField(verbose_name='Nombre', max_length=70)
    last_name = models.CharField(verbose_name='Apellidos', max_length=70)
    job = models.CharField(verbose_name='Trabajo', max_length=60, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    full_name = models.CharField(verbose_name='Nombre completo',max_length=140,blank=True)#No funciona
    

    

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']

    def __str__(self):
        return str(self.id) + ' - ' +  self.first_name + ' - ' + self.last_name


    

    
