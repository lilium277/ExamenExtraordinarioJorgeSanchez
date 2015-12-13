from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Clientes
from clientes.forms import ClientesForm

# Create your views here.
def listar_usuario(request):
	clientes = Clientes.objects.all()
	return render(request, 'clientes/lista_clientes.html', {'clientes':clientes})