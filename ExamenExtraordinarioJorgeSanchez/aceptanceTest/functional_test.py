from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.alert import Alert
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_add_pelicula_from_lista_existencias(self):
    	#entra a la opcion listar peliculas
        self.browser.get('http://192.168.0.24:8001/peliculas/lista_existencias')

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

    def test_can_edit_pelicula_from_lista_existencias(self):
            #entra a la opcion listar peliculas
            self.browser.get('http://192.168.0.24:8001/peliculas/lista_existencias')

            #comprueba que esta en la lista de peliculas en existencia
            self.assertIn(u'Peliculas en existencia', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Lista de Peliculas existentes',header_text)

            #busca la opcion eliminar de la pelicula volver al futuro 3 y la activa
            button = self.browser.find_element_by_name('editar_pelicula_Volver al futuro 3')
            button.send_keys(Keys.ENTER)
            Alert(driver).accept()

            self.assertIn(u'Pelicula Actualizar', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Actualizar Pelicula',header_text)        

            #busca las cajas para capturar la informacion a modificar
            textBox = self.browser.find_element_by_id('id_sinopsis')
            textBox.send_keys('Viaje al pasado protagonizado por Michael J. Fox')

            #presiona el boton para salvar los cambios en el campo sinopsis
            button = self.browser.find_element_by_name('Guardar_Pelicula')
            button.send_keys(Keys.ENTER)
            
            #busca la nueva pelicula guardada
            table = self.browser.find_element_by_tag_name('div')
            rows = table.find_elements_by_tag_name('li')
            self.assertTrue(
                any(row.text == 'Viaje al pasado protagonizado por Michael J. Fox' for row in rows)
            )        


if __name__ == '__main__':  
    unittest.main() 