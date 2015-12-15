from django.conf.urls import url
from empleados.views import listar_empleado, nuevo_usuario, iniciar_sesion, homepage

urlpatterns = [
    url(r'^listar_empleado$', listar_empleado, name="listar_empleado"),
    url(r'^nuevo_usuario/$', nuevo_usuario, name = "nuevo_usuario"),
    url(r'^login/$', iniciar_sesion, name = "iniciar_sesion"),
    url(r'^$', homepage, name = "homepage"),
]