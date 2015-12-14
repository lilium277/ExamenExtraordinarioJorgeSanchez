Feature: Como empleado del videoclub
		Quiero eliminar películas que se encuentren dañadas o se hayan perdido
		Para tener el inventario actualizado

Scenario: Eliminar la pelicula volver al futuro 2
	Given Que selecciono la opcion "eliminar_pelicula_" de la pelicula "volver al futuro 2" 
	When Clickeo el boton eliminar
	Then no puedo ver en la lista de peliculas la pelicula "volver al futuro 2"