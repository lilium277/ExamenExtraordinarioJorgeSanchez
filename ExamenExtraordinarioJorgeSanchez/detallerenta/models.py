from django.db import models
from peliculas.models import Peliculas
from rentas.models import Rentas

# Create your models here.
class DetallesRentas(models.Model):
	fecha_entrega = models.DateField('Fecha de renta')
	pelicula = models.ForeignKey(Peliculas)
	renta = models.ForeignKey(Rentas)

	def __str__(self):
		return self.titulo