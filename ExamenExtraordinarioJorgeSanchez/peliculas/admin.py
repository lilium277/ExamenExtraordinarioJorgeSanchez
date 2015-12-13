from django.contrib import admin
from peliculas.models import Peliculas, Genero, Clasificacion

# Register your models here.
admin.site.register(Peliculas)
admin.site.register(Genero)
admin.site.register(Clasificacion)