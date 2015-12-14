from django.conf.urls import url
from empleados.views import listar_empleado, nuevo_usuario, iniciar_sesion, main

urlpatterns = [
    url(r'^$', listar_empleado, name="listar_empleado"),
    #usuarios
    url(r'^nuevo_usuario/$', nuevo_usuario, name = "nuevo_usuario"),
    url(r'^login/$', iniciar_sesion, name = "iniciar_sesion"),
    url(r'^iniciar_sesion$', main, name = "main"),
]