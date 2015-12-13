from django.conf.urls import url
from clientes.views import listar_usuario

urlpatterns = [
    url(r'^$', listar_usuario, name="listar_usuario"),
]