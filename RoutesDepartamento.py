from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from __main__ import app

from Controladores.ControladorDepartamento import ControladorDepartamento
miControladorDepartamento=ControladorDepartamento()

@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    json=miControladorDepartamento.index()
    if not json:
        return {"No se encuentra ningun Departamento en la Base de Datos"}
    else:
        return jsonify(json)
@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    if json:
        return jsonify(json)
        return {"Departamento creado exitosamente"}
    else:
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    if not json:
        return {"No se encuentra ningun Departamento para el id en la Base de Datos"}
    else:
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    if not json:
        return {"Error al actualizar el Departamento"}
    else:
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
    if not json:
        return {"Error al eliminar el Departamento"}
    else:
        return jsonify(json)
