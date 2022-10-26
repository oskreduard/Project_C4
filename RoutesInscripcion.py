from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorInscripcion import ControladorInscripcion
miControladorInscripcion=ControladorInscripcion()
from Controladores.ControladorMateria import ControladorMateria
miControladorMateria=ControladorMateria()
from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()

@app.route("/inscripciones",methods=['GET'])
def getinscripciones():
    json=miControladorInscripcion.index()
    if not json:
        json = {}
        json["message"] = "No se encuentra ninguna Inscripcion en la Base de Datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    validacion1 = miControladorMateria.show(id_materia)
    validacion2 = miControladorEstudiante.show(id_estudiante)
    if validacion1 == {} or validacion2 == {}:
        json = {}
        return {"Resultado": "No se encuentran la Materia o el Estudiante indicados"}
    else:
        data = request.get_json()
        json=miControladorInscripcion.create(data,id_estudiante,id_materia)
        return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    if json == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Inscripcion para el Id en la Base de datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    validacion1 = miControladorInscripcion.show(id_inscripcion)
    validacion2 = miControladorMateria.show(id_materia)
    validacion3 = miControladorEstudiante.show(id_estudiante)
    if validacion1 == {} or validacion2 == {} or validacion3 == {}:
        json = {}
        return {"Resultado": "No se encuentran los datos indicados indicados"}
    else:
        data = request.get_json()
        json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
        return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['DELETE'])
def eliminarInscripcion(id):
    validacion = miControladorInscripcion.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Inscripcion para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json = miControladorInscripcion.delete(id)
        return jsonify(json)

@app.route("/inscripciones/All", methods=['DELETE'])
def eliminarTodaslasInscripciones():
    validacion = miControladorInscripcion.index()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Inscripciones en la base de datos!"}
    else:
        result = miControladorInscripcion.delete_all()
        return result

