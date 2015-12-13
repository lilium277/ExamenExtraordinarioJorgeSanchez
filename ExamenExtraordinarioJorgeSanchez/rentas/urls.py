from django.conf.urls import url
from rentas.views import listar_rentas, renta_nueva

urlpatterns = [
    url(r'^$', listar_rentas, name="lista_rentas"),
    url(r'^renta_nueva/$', renta_nueva, name = "renta_nueva"),
]