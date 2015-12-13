from django.shortcuts import render, redirect, get_object_or_404
from rentas.models import Rentas
from rentas.forms import RentasForm

# Create your views here.
def listar_rentas(request):
	rentas = Rentas.objects.all()
	return render(request, 'rentas/lista_rentas.html', {'rentas':rentas})

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