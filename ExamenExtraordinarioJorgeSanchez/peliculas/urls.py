from django.conf.urls import url
from peliculas.views import listar_peliculas, listar_peliculas_renta, nueva_pelicula, eliminar_pelicula, editar_pelicula
urlpatterns = [
    url(r'^lista_existencias$', listar_peliculas, name="lista_peliculas"),
    url(r'^lista_peliculas$', listar_peliculas_renta, name="lista_peliculas_renta"),
    url(r'^nueva_pelicula/$', nueva_pelicula, name = "nueva_pelicula"),
    url(r'^(?P<pk>[0-9]+)/eliminar_pelicula', eliminar_pelicula, name= "eliminar_pelicula"),
    url(r'^(?P<pk>[0-9]+)/editar_pelicula', editar_pelicula, name= "editar_pelicula"),
]