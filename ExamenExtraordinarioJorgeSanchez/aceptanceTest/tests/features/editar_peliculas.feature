Feature: Como empleado del videoclub
		Quiero edItar películas que tengan datos incorrectos
		Para tener el inventario actualizado


Scenario: Editar la pelicula volver al futuro
	Given Que selecciono la opcion "editar_pelicula_" de la pelicula "volver al futuro 2" y cambio el campo descripcion por "La segunda de 3"
	When Oprimo el boton de guardar
	Then puedo ver en la sinopsis "La segunda de 3"