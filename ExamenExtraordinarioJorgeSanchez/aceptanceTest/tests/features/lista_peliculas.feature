Feature: Como empleado del videoclub
		Quiero visualizar la lista de películas
		Para conocer en todo momento el inventario existente

Scenario: Entrar a la lista de peliculas y encontrar la pelicula volver al futuro 3
	Given Que enntro a la direccion "http://192.168.0.24:8000/peliculas/" 
	When cuando doy enter en la barra de navegacion
	Then puedo ver en la lista de peliculas la pelicula "volver al futuro 3"