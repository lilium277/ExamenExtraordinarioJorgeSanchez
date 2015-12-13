# coding: utf-8
from django import forms
from peliculas.models import Peliculas

class PeliculasForm(forms.ModelForm):

	class Meta(object):
		model = Peliculas
		fields = ['clave', 'titulo', 'duracion', 'sinopsis', 'genero', 'clasificacion']