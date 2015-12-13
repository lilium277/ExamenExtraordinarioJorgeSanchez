from django.db import models
from clientes.models import Clientes

# Create your models here.
class Rentas(models.Model):
	fecha_renta = models.DateField('Fecha de renta')
	cliente = models.ForeignKey(Clientes)

	def __str__(self):
		return self.fecha_renta