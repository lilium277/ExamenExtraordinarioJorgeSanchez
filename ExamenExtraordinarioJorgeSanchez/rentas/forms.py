# coding: utf-8
from django import forms
from rentas.models import Rentas

class RentasForm(forms.ModelForm):

	class Meta(object):
		model = Rentas
		fields = ['fecha_renta','cliente']