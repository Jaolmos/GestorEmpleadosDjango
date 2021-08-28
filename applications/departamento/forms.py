from django import forms



class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=70)
    apellidos = forms.CharField(max_length=70)
    departamento = forms.CharField(max_length=70)
    nombre_corto = forms.CharField(max_length=50)