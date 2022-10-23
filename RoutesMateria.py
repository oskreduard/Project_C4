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
        return {"No se encuentra ninguna Materia en la Base de Datos"}
    else:
        return jsonify(json)
@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    if json:
        return jsonify(json)
        return {"Materia creado exitosamente"}
    else:
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    if not json:
        return {"No se encuentra una Materia para el Id en la Base de datos"}
    else:
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorMateria.update(id,data)
    if not json:
        return {"Error al actualizar la Materia"}
    else:
        return jsonify(json)
@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorMateria.delete(id)
    if not json:
        return {"Error al Eliminar la Materia"}
    else:
        return jsonify(json)

