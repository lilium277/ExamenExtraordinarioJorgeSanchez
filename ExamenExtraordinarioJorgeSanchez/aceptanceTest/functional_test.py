from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_list_movies_and_interact(self):
    	#entra a la opcion listar peliculas
        self.browser.get('http://192.168.0.24:8000/peliculas/')

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

        #elimina la nueva pelicula guardada
        """button = self.browser.find_element_by_name('elimina_pelicula_Volver al futuro 3')
        button.send_keys(Keys.ENTER)"""



if __name__ == '__main__':  
    unittest.main() 