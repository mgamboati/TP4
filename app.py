'''________________________________________________________________________
					
					Instituto Tecnologico de Costa Rica
					     Lenguajes de Programacion	
					     Segunda Tarea Programada 
					     App Web en Python
					
					Realizado por: 
					        * Josue Espinoza Castro 
						* Mauricio Gamboa Cubero
						* Andres Pacheco Quesada

					Junio del 2014
__________________________________________________________________________'''

#Imports del framework para la aplicacion web: Flask
from flask import Flask
from flask import request, redirect, url_for, abort, session
from flask import render_template

#Imports para usar el API de GoogleMaps
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

#Nombre de la aplicacion: Bumbur
app = Flask("Apartas")
GoogleMaps(app)

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------	FRONTEND           ------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#URL y funcion para home
@app.route('/')
def mapview():
# creating a map in the view
	mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)])
	return render_template('example.html', mymap=mymap)

#URL y funcion para la pagina de consultar
@app.route('/consultar')
def consultar():
	return render_template('consultar.html')

#URL y funcion para la pagina de ingresar datos
@app.route('/mantenimiento')
def mantenimiento():
    return render_template('mantenimiento.html')
   
#URL y funcion para la pagina de ingresar platillos 
@app.route('/platillo')
def platillo():
    return render_template('platillo.html')

#URL y funcion para la pagina de ingresar un nuevo restaurante 
@app.route('/newRestaurante', methods=['POST'])
def newRestaurante():
    Nombre = request.form['nombre']
    TipoDeComida = request.form['tipoDeComida']
    Ubicacion = request.form['ubicacion']
    Telefono = request.form['telefono']
    Horario = request.form['horario']
    nuevoRestaurante(Nombre,TipoDeComida,Ubicacion,Telefono,Horario)
    return render_template('felicidades.html')

#URL y funcion para la pagina de ingresar un nuevo platillo 
@app.route('/newPlatillo', methods=['POST'])
def newPlatillo():
    Restaurante = request.form['restaurante']
    Nombre = request.form['nombre']
    Tipo = request.form['tipo']
    Pais = request.form['pais']
    Receta = request.form['receta']
    nuevaComida(Restaurante,Nombre,Tipo,Pais,Receta)
    return render_template('felicidades.html')    

#-----------------------------------------------CONSULTAS-----------------------------------------------

#URL y funcion para la pagina de consultar todos los restaurantes
@app.route('/consultarTodosRestaurantes')
def consultarTodosRestaurantes():
	lista = consultaRestaurantes()
	if lista == []:
		lista.append("No se encontro restaurantes.")
	return render_template('mostrarConsulta.html',lista=lista)

#URL y funcion para la pagina de pedirle al usuario un nombre del restaurante
@app.route('/nombreAConsultar')
def nombreAConsultar():
    return render_template('nombreAConsultar.html')

#URL y funcion para la pagina de consultar restaurantes por nombre       
@app.route('/consultarRestaurantesPorNombre', methods=['POST'])
def consultarRestaurantesPorNombre():
	nombre = request.form['nombreRest']
	lista = consultaNombre(nombre)
	if lista == []:
		lista.append("No se encontro restaurantes con ese nombre.")
	return render_template('mostrarConsulta.html',lista=lista)

#URL y funcion para la pagina de pedirle al usuario un nombre del restaurante		
@app.route('/tipoAConsultar')
def tipoAConsultar():
    return render_template('tipoAConsultar.html')

#URL y funcion para la pagina de consultar todos los restaurantes segun un tipo de comida
@app.route('/consultarRestaurantesPorTipo', methods=['POST'])
def consultarRestaurantesPorTipo():
	tipo = request.form['tipo']
	lista = consultaTipo(tipo)
	if lista == []:
		lista.append("No se encontro restaurantes con ese tipo de comida.")
	return render_template('mostrarConsulta.html',lista=lista)
	
#URL y funcion para la pagina de pedirle al usuario un nombre del restaurante	
@app.route('/paisAConsultar')
def paisAConsultar():
    return render_template('paisAConsultar.html')

#URL y funcion para la pagina de consultar todos los restaurantes con comidas de un pais    	
@app.route('/consultarRestaurantesPorPais', methods=['POST'])
def consultarRestaurantesPorPais():
	pais = request.form['pais']
	lista = consultaPlatilloPais(pais)
	if len(lista) == 1:
		lista.append("No se encontro restaurantes con platillos de ese pais.")
	return render_template('mostrarConsulta.html',lista=lista)
	
#URL y funcion para la pagina de pedirle al usuario un nombre del restaurante		
@app.route('/restauranteAConsultar')
def restauranteAConsultar():
    return render_template('restauranteAConsultar.html')

#URL y funcion para la pagina de consultar todos los platillos de un restaurante   
@app.route('/consultarPlatillosPorRestaurante', methods=['POST'])
def consultarPlatillosPorRestaurante():
	restaurante = request.form['restaurante']
	lista = consultaPlatillosDeRestaurante(restaurante)
	if len(lista) == 1:
		lista.append("No se encontro platillos para ese restaurante.")
	return render_template('mostrarConsulta.html',lista=lista)

#URL y funcion para la pagina de pedirle al usuario un nombre del restaurante	
@app.route('/restEIngredienteAConsultar')
def restEIngredienteAConsultar():
    return render_template('restEIngredienteAConsultar.html')

#URL y funcion para la pagina de consultar todos los platillos de un restaurante con tal ingrediente   
@app.route('/consultarPlatillosPorRestEIng', methods=['POST'])
def consultarPlatillosPorRestEIng():
	restaurante = request.form['restaurante']
	ingrediente = request.form['ingrediente']
	lista = RestDeIng(restaurante,ingrediente)
	if lista == []:
		lista.append("No se encontro platillos de ese restaurante con ese ingrediente.")
	return render_template('mostrarConsulta.html',lista=lista)

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------		BACKEND         ---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- 		  MAIN		    -----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#main de la aplicacion
if __name__ == '__main__':
	#app.debug = True
	app.run(host='172.19.14.89')#CAMBIAR ESTE IP POR EL ACTUAL
