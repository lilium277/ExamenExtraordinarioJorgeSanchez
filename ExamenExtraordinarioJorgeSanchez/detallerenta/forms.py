# coding: utf-8
from django import forms
from detallerenta.models import DetallesRentas

class DetallesRentasForm(forms.ModelForm):

	class Meta(object):
		model = DetallesRentas
		fields = ['fecha_entrega','pelicula','renta']