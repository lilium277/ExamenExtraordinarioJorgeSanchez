from django.shortcuts import render
from detallerenta.models import DetallesRentas
from detallerenta.forms import DetallesRentasForm
# Create your views here.
def listar_detalles(request):
	detalles = DetallesRentas.objects.all()
	return render(request, 'detallerenta/lista_detalles.html', {'detalles':detalles})

def renta_nueva(request):
	if request.method == "POST":
		form = RentasForm(request.POST)
		print request.POST
		if form.is_valid():
			renta = form.save()
			renta.save()
			return redirect('lista_rentas')
	else:
		form = RentasForm
	return render(request,'rentas/renta_nueva.html',{'form':form, 'etiqueta':'Nueva'})