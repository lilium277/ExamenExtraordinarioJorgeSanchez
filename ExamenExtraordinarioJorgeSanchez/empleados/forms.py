# coding: utf-8
from django import forms
from empleados.models import Empleados

class EmpleadosForm(forms.ModelForm):
	""" Formulario para dar servicio al modelo Clientes"""

	class Meta(object):
		model = Empleados
		fields = ['RFC', 'user']