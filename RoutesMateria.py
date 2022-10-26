from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorMateria import ControladorMateria
miControladorMateria=ControladorMateria()

@app.route("/materias",methods=['GET'])
def getmaterias():
    json=miControladorMateria.index()
    if not json:
        json = {}
        json["message"] = "No se encuentra ninguna Materia en la Base de Datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    if json:
        json = {}
        json["message"] = "Materia creada exitosamente"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    if json == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Materia para el Id en la Base de datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    validacion = miControladorMateria.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Materia para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json = miControladorMateria.update(id, data)
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    validacion = miControladorMateria.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ninguna Materia para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json = miControladorMateria.delete(id)
        return jsonify(json)

@app.route("/materias/All", methods=['DELETE'])
def eliminarTodaslasMaterias():
    validacion = miControladorMateria.index()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Materias en la base de datos!"}
    else:
        result = miControladorMateria.delete_all()
        return result

