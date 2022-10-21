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
    return jsonify(json)
@app.route("/inscripciones",methods=['POST'])
def crearInscripcion():
    data = request.get_json()
    json=miControladorInscripcion.create(data)
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['PUT'])
def modificarInscripcion(id):
    data = request.get_json()
    json=miControladorInscripcion.update(id,data)
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['DELETE'])
def eliminarInscripcion(id):
    json=miControladorInscripcion.delete(id)
    return jsonify(json)
