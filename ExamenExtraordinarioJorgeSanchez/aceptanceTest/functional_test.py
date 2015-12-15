from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.alert import Alert
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()


    def test_can_edit_pelicula_from_lista_existencias(self):
            #entra a la opcion listar peliculas 
            #self.browser.get('http://192.168.0.24:8001/peliculas/lista_existencias')
            self.browser.get('http://10.2.48.179:8000/peliculas/lista_existencias')
            #comprueba que esta en la lista de peliculas en existencia
            self.assertIn(u'Peliculas en existencia', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Lista de Peliculas existentes',header_text)

            #busca la opcion eliminar de la pelicula volver al futuro 3 y la activa
            button = self.browser.find_element_by_name('editar_pelicula_Volver al futuro 3')
            button.send_keys(Keys.ENTER)
            Alert(self.browser).accept()

            self.assertIn(u'Pelicula Actualizar', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Actualizar Pelicula',header_text)        

            #busca las cajas para capturar la informacion a modificar
            textBox = self.browser.find_element_by_id('id_sinopsis')
            textBox.clear()
            textBox.send_keys('Viaje al pasado protagonizado por Michael J. Fox')

            #presiona el boton para salvar los cambios en el campo sinopsis
            button = self.browser.find_element_by_name('Guardar_Pelicula')
            button.send_keys(Keys.ENTER)
            
            #busca la nueva pelicula guardada
            table = self.browser.find_elements_by_class_name('sinopsis')
            tableTexts = [row.text for row in table]
            self.assertIn('sinopsis: Viaje al pasado protagonizado por Michael J. Fox', tableTexts,"esperado "+str(tableTexts))

    def test_can_delete_pelicula_from_lista_existencias(self):
            #entra a la opcion listar peliculas 
            #self.browser.get('http://192.168.0.24:8001/peliculas/lista_existencias')
            self.browser.get('http://10.2.48.179:8000/peliculas/lista_existencias')
            #comprueba que esta en la lista de peliculas en existencia
            self.assertIn(u'Peliculas en existencia', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Lista de Peliculas existentes',header_text)

            #busca la opcion eliminar de la pelicula volver al futuro 3 y la activa
            button = self.browser.find_element_by_name('eliminar_pelicula_Volver al futuro 3')
            button.send_keys(Keys.ENTER)       
            Alert(self.browser).accept()

            self.assertIn(u'Peliculas en existencia', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Lista de Peliculas existentes',header_text)
            
            #busca la nueva pelicula guardada
            table = self.browser.find_elements_by_tag_name('li')
            tableTexts = [row.text for row in table]
            self.assertNotIn('Clave: 6', tableTexts,"esperado "+str(tableTexts))


if __name__ == '__main__':
    unittest.main() 