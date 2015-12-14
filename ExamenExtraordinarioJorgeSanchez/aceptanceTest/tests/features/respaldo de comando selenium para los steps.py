@step(u'Given Que ingreso la clave "([^"]*)", el titulo "([^"]*)", la descripcion "([^"]*)", la duracion "([^"]*)", la sinopsis "([^"]*)", el genero "([^"]*)" y la clasificacion "([^"]*)"  en la caja de texto')
def given_que_ingreso_la_pelicula_group1_en_las_cajas_de_texto(step, clave, titulo, descripcion, duracion, sinopsis, genero, clasificacion):
    world.driver = webdriver.Firefox()
    world.driver.get("http://192.168.0.24:8000/peliculas/nueva_pelicula/")
    caja = world.driver.find_element_by_id("id_clave")
    caja.send_keys(clave)
    caja = world.driver.find_element_by_id("id_titulo")
    caja.send_keys(titulo)
    caja = world.driver.find_element_by_id("id_duracion")
    caja.send_keys(duracion)
    caja = world.driver.find_element_by_id("id_sinopsis")
    caja.send_keys(sinopsis)
    caja = world.driver.find_element_by_id("id_genero")
    caja.send_keys(genero)
    caja = world.driver.find_element_by_id("id_clasificacion")
    caja.send_keys(clasificacion)

@step(u'When Oprimo el botón de guardar')
def when_oprimo_el_boton_de_guardar(step):
    boton = world.driver.find_element_by_value("Guardar")
    boton.click()

@step(u'Then Puedo ver el titulo "([^"]*)" en la lista de peliculas guardadas')
def then_puedo_ver_el_titulo_group1_en_la_lista_de_peliculas_guardadas(step, esperado):
    pelicula = world.driver.find_elements_by_tag_name('h3')
    peliculasText = [peli.text for peli in pelicula]
    print peliculasText
    assert esperado in peliculasText, "No se encuentra la pelicula"+esperado+" en la lista"+str(peliculasText)