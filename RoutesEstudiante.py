from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()

@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    if not json:
        json = {}
        json["message"] = "No se encuentra ningun Estudiante en la Base de Datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    if json:
        json = {}
        json["message"] = "Estudiante creado exitosamente"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    if json == {}:
        json = {}
        json["message"] = "No se encuentra ningun estudiante para el Id en la Base de datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    validacion = miControladorEstudiante.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun estudiante para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json=miControladorEstudiante.update(id,data)
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    validacion = miControladorEstudiante.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun estudiante para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json=miControladorEstudiante.delete(id)
        return jsonify(json)
@app.route("/estudiantes/All", methods=['DELETE'])
def eliminarTodosLosResultados():
    validacion = miControladorEstudiante.index()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Estudiantes en la base de datos!"}
    else:
        result = miControladorEstudiante.delete_all()
        return result
