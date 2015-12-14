from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from empleados.models import Empleados
from empleados.forms import EmpleadosForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def listar_empleado(request):
	empleados = Empleados.objects.all()
	return render(request, 'empleados/lista_empleados.html', {'empleados':empleados})

def nuevo_usuario(request):
	if request.method == "POST":
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/listar_empleado')
	else:
		formulario = UserCreationForm()
		return render_to_response('empleados/nuevo_usuario.html',{'formulario':formulario},context_instance=RequestContext(request))

def iniciar_sesion(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('empleados/nuevo_usuario.html')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = username, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('peliculas/lista_peliculas.html')
				else:
					return HttpResponseRedirect('empleados/nuevo_usuario.html')
			else:
				return HttpResponseRedirect('empleados/nuevo_usuario.html')
	else:
		formulario = AuthenticationForm()
	return render_to_response('empleados/login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def main(request):
	return render(request,'empleados/iniciar_sesion.html')