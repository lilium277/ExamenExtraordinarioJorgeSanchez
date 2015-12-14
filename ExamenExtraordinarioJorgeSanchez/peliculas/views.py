from django.shortcuts import render, redirect, get_object_or_404
from peliculas.models import Peliculas
from peliculas.forms import PeliculasForm
from django.contrib.auth.decorators import permission_required

# Create your views here.
def listar_peliculas(request):
	peliculas = Peliculas.objects.all()
	#return render(request, 'peliculas/lista_peliculas_para_renta.html', {'peliculas':peliculas})
	return render(request, 'peliculas/lista_peliculas.html', {'peliculas':peliculas})

#@permission_required('usuarios.can_add','index')
def nueva_pelicula(request):
	if request.method == "POST":
		form = PeliculasForm(request.POST)
		print request.POST
		if form.is_valid():
			pelicula = form.save()
			pelicula.save()
			return redirect('lista_peliculas')
	else:
		form = PeliculasForm
	return render(request,'peliculas/pelicula_nueva.html',{'form':form, 'etiqueta':'Nueva'})

def eliminar_pelicula(request, pk):
	peliculas = get_object_or_404(Peliculas, pk = pk)
	peliculas.delete()
	return redirect('lista_peliculas')

def editar_pelicula(request, pk):
	peliculas = get_object_or_404(Peliculas, pk = pk)
	if request.method == "POST":
		form = PeliculasForm(request.POST, instance = peliculas)
		print request.POST
		if form.is_valid():
			peliculas = form.save()
			peliculas.save()
			return redirect('lista_peliculas')
	else:
		form = PeliculasForm (instance=peliculas)
	return render(request,'peliculas/pelicula_nueva.html',{'form':form, 'etiqueta':'Actualizar'})
