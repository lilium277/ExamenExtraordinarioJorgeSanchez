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

    """def test_can_add_pelicula_from_lista_existencias(self):
        #entra a la opcion listar peliculas
        #self.browser.get('http://192.168.0.24:8001/peliculas/lista_existencias')
        self.browser.get('http://10.2.48.179:8000/peliculas/lista_existencias')

        #comprueba que esta en la lista de peliculas en existencia
        self.assertIn(u'Peliculas en existencia', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lista de Peliculas existentes',header_text)

        #busca un boton con el texto Nueva Pelicula
        buttons = self.browser.find_elements_by_tag_name('button')        
        self.assertTrue(
                any(button.text == 'Nueva Pelicula' for button in buttons)
        )

        #presiona el boton para entrar al formulario para insertar una pelicula
        button = self.browser.find_element_by_tag_name('button')
        button.send_keys(Keys.ENTER)

        #comprobamos que vaya a la pagina para agregar una pelicula nueva
        self.assertIn(u'Pelicula Nueva', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Nueva Pelicula',header_text)

        #busca las cajas para capturar la informacion de la nueva pelicula e inserta datos
        textBox = self.browser.find_element_by_id('id_clave')
        textBox.send_keys('6')
        textBox = self.browser.find_element_by_id('id_titulo')
        textBox.send_keys('Volver al futuro 3')
        textBox = self.browser.find_element_by_id('id_duracion')
        textBox.send_keys(120)
        textBox = self.browser.find_element_by_id('id_sinopsis')
        textBox.send_keys('Tercera y ultima pelicula de la trilogia protagonizada por Michael J. Fox')
        textBox = self.browser.find_element_by_id('id_genero')
        textBox.send_keys('ciencia ficcion')
        textBox = self.browser.find_element_by_id('id_clasificacion')
        textBox.send_keys('B-15')

        button = self.browser.find_element_by_name('Guardar_Pelicula')
        button.send_keys(Keys.ENTER)
        
        #busca la nueva pelicula guardada
        table = self.browser.find_element_by_tag_name('div')
        rows = table.find_elements_by_tag_name('h3')
        self.assertTrue(
            any(row.text == 'Volver al futuro 3' for row in rows)
        )
