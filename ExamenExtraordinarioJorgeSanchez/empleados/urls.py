from django.conf.urls import url
from empleados.views import listar_empleado

urlpatterns = [
    url(r'^$', listar_empleado, name="listar_empleado"),
]