from django.shortcuts import render, redirect, get_object_or_404
from rentas.models import Rentas
from rentas.forms import RentasForm
from peliculas.models import Peliculas
from detallerenta.models import DetallesRentas
from datetime import datetime,timedelta

# Create your views here.
def listar_rentas(request):
	rentas = Rentas.objects.all()
	return render(request, 'rentas/lista_rentas.html', {'rentas':rentas})

def renta_nueva(request):
	if request.method == "POST":
		form = RentasForm(request.POST)
		peliculas = request.POST.getlist('peliculas')
		print (request.POST.getlist('peliculas'))
		print (request.POST)
		if form.is_valid():
			renta = form.save()
			renta.save()
			for pelicula in peliculas:
				pelicula_Temp = Peliculas.objects.get(id="peliculas.value")
				print (pelicula_Temp)
				print (renta)
				entrega= renta.fecha_renta + timedelta(days=3)
				detalles = DetallesRentas(fecha_entrega=entrega,pelicula=pelicula_Temp,renta=renta)
				detalles.save()
			return redirect('lista_rentas')
	else:
		form = RentasForm
	return render(request,'rentas/renta_nueva.html',{'form':form, 'etiqueta':'Nueva'})

"""def renta_nueva(request):
	if request.method == "POST":
		form = RentasForm(request.POST)
		print request.POST
		if form.is_valid():
			renta = form.save()
			renta.save()
			return redirect('lista_rentas')
	else:
		form = RentasForm
	return render(request,'rentas/renta_nueva.html',{'form':form, 'etiqueta':'Nueva'})"""