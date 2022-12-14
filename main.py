from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

import RoutesEstudiante
import RoutesMateria
import RoutesDepartamento
import RoutesInscripcion

'''Principal Route'''
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running mision tic 2022 final..."
    return jsonify(json)

''' Creating the server '''
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])