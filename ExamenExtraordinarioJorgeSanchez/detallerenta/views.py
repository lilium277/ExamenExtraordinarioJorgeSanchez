from django.shortcuts import render
from detallerenta.models import DetallesRentas
from detallerenta.forms import DetallesRentasForm
# Create your views here.
def listar_detalles(request):
	detalles = DetallesRentas.objects.all()
	return render(request, 'detallerenta/lista_detalles.html', {'detalles':detalles})