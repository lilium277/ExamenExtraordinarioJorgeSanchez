from django.shortcuts import render, redirect, get_object_or_404
from empleados.models import Empleados
from empleados.forms import EmpleadosForm

# Create your views here.
def listar_empleado(request):
	empleados = Empleados.objects.all()
	return render(request, 'empleados/lista_empleados.html', {'empleados':empleados})