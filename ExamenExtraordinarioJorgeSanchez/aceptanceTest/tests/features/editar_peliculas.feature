Feature: Como empleado del videoclub
		Quiero edItar películas que tengan datos incorrectos
		Para tener el inventario actualizado


Scenario: Editar la pelicula volver al futuro
	Given Que ingreso el cuadro de texto Clave: "4" y ingreso en la caja de texto Titulo: "volver al futuro" y en la caja de Duracion: "100" y en la caja de Sinopsis: "Primera pelicula de la trilogia con Michael J. Fox" y en la caja Genero: "Fantasia" y en la caja Clasificacion: "B"
	When Oprimo el boton de guardar
	Then puedo ver el titulo "volver al futuro" en la lista de peliculas guardadas

Scenario: Modificar la pelicula volver al futuro 2
	Given Que ingreso el cuadro de texto Clave: "5" y ingreso en la caja de texto Titulo: "volver al futuro 2" y en la caja de Duracion: "100" y en la caja de Sinopsis: "Segunda pelicula de la trilogia con Michael J. Fox" y en la caja Genero: "Fantasia" y en la caja Clasificacion: "B"
	When Oprimo el boton de guardar
	Then puedo ver el titulo "volver al futuro 2" en la lista de peliculas guardadas