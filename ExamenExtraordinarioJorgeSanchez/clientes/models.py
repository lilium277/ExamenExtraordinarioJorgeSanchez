from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clientes(User):	
	domicilio = models.CharField(max_length = 300)
	RFC = models.CharField(max_length = 13)
	celular = models.BigIntegerField(default = 0)
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user