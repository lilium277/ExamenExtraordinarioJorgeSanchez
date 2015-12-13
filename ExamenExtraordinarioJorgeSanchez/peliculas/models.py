from django.db import models

# Create your models here.
class Genero(models.Model):
	genero = models.CharField(max_length=65)

	def __str__(self):
		return self.genero


class Clasificacion(models.Model):
	clasificacion = models.CharField(max_length=65)

	def __str__(self):
		return self.clasificacion

class Peliculas(models.Model):
	clave = models.IntegerField(default = 0)
	titulo = models.CharField(max_length = 125)
	duracion = models.IntegerField(default = 0)
	sinopsis = models.CharField(max_length=300)
	genero = models.ForeignKey(Genero)	
	clasificacion = models.ForeignKey(Clasificacion)

	def __str__(self):
		return self.titulo