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
        json = {}
        json["message"] = "No se encuentra ningun Departamento en la Base de Datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json = miControladorDepartamento.create(data)
    if json:
        json = {}
        json["message"] = "Departamento creado exitosamente"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    if json == {}:
        json = {}
        json["message"] = "No se encuentra ningun Departamento para el Id en la Base de datos"
        return jsonify(json)
    else:
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    validacion = miControladorDepartamento.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Departamento para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json=miControladorDepartamento.update(id,data)
        return jsonify(json)
@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    validacion = miControladorDepartamento.show(id)
    if validacion == {}:
        json = {}
        json["message"] = "No se encuentra ningun Departamento para el Id en la Base de datos"
        return jsonify(json)
    else:
        data = request.get_json()
        json = miControladorDepartamento.delete(id)
        return jsonify(json)

@app.route("/departamentos/All", methods=['DELETE'])
def eliminarTodosLosDepartamentos():
    validacion = miControladorDepartamento.index()
    if validacion == []:
        json = {}
        return {"Resultado": "No se encuentran Departamentos en la base de datos!"}
    else:
        result = miControladorDepartamento.delete_all()
        return result



