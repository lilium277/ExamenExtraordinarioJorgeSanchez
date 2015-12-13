# coding: utf-8
from django import forms
from clientes.models import Clientes

class ClientesForm(forms.ModelForm):
	""" Formulario para dar servicio al modelo Clientes"""

	class Meta(object):
		model = Clientes
		fields = ['domicilio', 'RFC', 'celular', 'user']