from django.conf.urls import url
from detallerenta.views import listar_detalles

urlpatterns = [
    url(r'^$', listar_detalles, name="lista_detalles"),
    #url(r'^renta_nueva/$', renta_nueva, name = "renta_nueva"),
]