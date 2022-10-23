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
        return {"No se encuentra ninguna Inscripción en la Base de Datos"}
    else:
        return jsonify(json)
@app.route("/inscripciones",methods=['POST'])
def crearInscripcion():
    data = request.get_json()
    json=miControladorInscripcion.create(data)
    if json:
        return jsonify(json)
        return {"Inscripción creado exitosamente"}
    else:
        return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    if not json:
        return {"No se encuentra una Inscripción para el Id en la Base de datos"}
    else:
        return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['PUT'])
def modificarInscripcion(id):
    data = request.get_json()
    json=miControladorInscripcion.update(id,data)
    if not json:
        return {"Error al actualizar la Inscripción"}
    else:
        return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['DELETE'])
def eliminarInscripcion(id):
    if not json:
        return {"Error al Eliminar la Inscripción"}
    else:
        return jsonify(json)
