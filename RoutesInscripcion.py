from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorInscripcion import ControladorInscripcion
miControladorInscripcion=ControladorInscripcion()

@app.route("/inscripciones",methods=['GET'])
def getinscripciones():
    json=miControladorInscripcion.index()
    if not json:
        json = {}
        json["message"] = "No se encuentra ninguna Inscripcion en la Base de Datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/inscripciones",methods=['POST'])
def crearInscripcion():
    data = request.get_json()
    json=miControladorInscripcion.create(data)
    if json:
        json = {}
        json["message"] = "Inscripcion creada exitosamente"
        return jsonify(json)
    else:
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
@app.route("/inscripciones/<string:id>",methods=['PUT'])
def modificarInscripcion(id):
    validacion = miControladorInscripcion.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Inscripcion para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json = miControladorInscripcion.update(id, data)
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

