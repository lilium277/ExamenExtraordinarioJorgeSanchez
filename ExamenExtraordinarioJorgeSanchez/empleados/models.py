from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleados(models.Model):
	RFC = models.CharField(max_length = 13)
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username