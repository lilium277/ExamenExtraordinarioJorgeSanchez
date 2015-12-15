# -*- coding: utf-8 -*-
from lettuce import step,world
from selenium import webdriver

@step(u'Given Que ingreso el cuadro de texto Clave: "([^"]*)" y ingreso en la caja de texto Titulo: "([^"]*)" y en la caja de Duracion: "([^"]*)" y en la caja de Sinopsis: "([^"]*)" y en la caja Genero: "([^"]*)" y en la caja Clasificacion: "([^"]*)"')
def given_que_ingreso_el_cuadro_de_texto_clave_group1_y_ingreso_en_la_caja_de_texto_titulo_group2_y_en_la_caja_de_duracion_group3_y_en_la_caja_de_sinopsis_group4_y_en_la_caja_genero_group5_y_en_la_caja_clasificacion_group6(step, group1, group2, group3, group4, group5, group6):
    world.driver = webdriver.Firefox()
    #world.driver.get('http://192.168.0.24:8000/peliculas/')
    world.driver.get('http://10.2.48.179:8000/peliculas/lista_existencias')
    button = world.driver.find_element_by_tag_name('button')
    button.send_keys(Keys.ENTER)

    textBox = world.driver.find_element_by_id('id_clave')
    textBox.send_keys(group1)
    textBox = world.driver.find_element_by_id('id_titulo')
    textBox.send_keys(group2)
    textBox = world.driver.find_element_by_id('id_duracion')
    textBox.send_keys(group3)
    textBox = world.driver.find_element_by_id('id_sinopsis')
    textBox.send_keys(group4)
    textBox = world.driver.find_element_by_id('id_genero')
    textBox.send_keys(group5)
    textBox = world.driver.find_element_by_id('id_clasificacion')
    textBox.send_keys(group6)

@step(u'When Oprimo el boton de guardar')
def when_oprimo_el_boton_de_guardar(step):
    button = world.driver.find_element_by_name('Guardar_Pelicula')
    button.send_keys(Keys.ENTER)

@step(u'Then puedo ver el titulo "([^"]*)" en la lista de peliculas guardadas')
def then_puedo_ver_el_titulo_group1_en_la_lista_de_peliculas_guardadas(step, group1):
    table = world.driver.find_element_by_tag_name('div')
    rows = table.find_elements_by_tag_name('h3')
    self.assertTrue(
        any(row.text == group1 for row in rows)
    )


@step(u'Given Que selecciono la opcion "([^"]*)" de la pelicula "([^"]*)" y cambio el campo descripcion por "([^"]*)"')
def given_que_selecciono_la_opcion_group1_de_la_pelicula_group2_y_cambio_el_campo_descripcion_por_group3(step, group1, group2, group3):
    assert False, 'This step must be implemented'
@step(u'Then puedo ver en la descripcion "([^"]*)"')
def then_puedo_ver_en_la_descripcion_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'Given Que selecciono la opcion "([^"]*)" de la pelicula "([^"]*)"')
def given_que_selecciono_la_opcion_group1_de_la_pelicula_group2(step, group1, group2):
    assert False, 'This step must be implemented'
@step(u'When Clickeo el boton eliminar')
def when_clickeo_el_boton_eliminar(step):
    assert False, 'This step must be implemented'
@step(u'Then no puedo ver en la lista de peliculas la pelicula "([^"]*)"')
def then_no_puedo_ver_en_la_lista_de_peliculas_la_pelicula_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'Given Que enntro a la direccion "([^"]*)"')
def given_que_enntro_a_la_direccion_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'When cuando doy enter en la barra de navegacion')
def when_cuando_doy_enter_en_la_barra_de_navegacion(step):
    assert False, 'This step must be implemented'
@step(u'Then puedo ver en la lista de peliculas la pelicula "([^"]*)"')
def then_puedo_ver_en_la_lista_de_peliculas_la_pelicula_group1(step, group1):
    assert False, 'This step must be implemented'