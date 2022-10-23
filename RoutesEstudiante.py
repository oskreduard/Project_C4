from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()

print("test1")
@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    if not json:
        return {"No se encuentra ningun Estudiante en la Base de Datos"}
    else:
        return jsonify(json)
@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    if json:
        return jsonify(json)
        return {"Estudiante creado exitosamente"}
    else:
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    if not json:
        return {"No se encuentra un Estudiante para el Id en la Base de datos"}
    else:
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    if not json:
        return {"Error al actualizar el Estudiante"}
    else:
        return jsonify(json)
@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    if not json:
        return {"Error al Eliminar el Estudiante"}
    else:
        return jsonify(json)
