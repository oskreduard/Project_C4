from Modelos.Departamento import Departamento
class ControladorDepartamento():

    def __init__(self):
        print("Creando ControladorDepartamento")

    def index(self):
        print("Listar todos los Departamentos")
        Departamentos = {
            "_id": "abc123",
            "departamento": "Areas Comunes",
        }
        return [Departamentos]

    def create(self, infoDepartamento):
        print("Crear un Departamento")
        elDepartamento = Departamento(infoDepartamento)
        return elDepartamento.__dict__

    def show(self, id):
        print("Mostrando un Departamento con id ", id)
        elDepartamento = {
            "_id": id,
            "departamento": "Areas Comunes",
        }
        return elDepartamento

    def update(self, id, infoDepartamento):
        print("Actualizando Departamento con id ", id)
        elDepartamento = Departamento(infoDepartamento)
        return elDepartamento.__dict__

    def delete(self, id):
        print("Elimiando Departamento con id ", id)
        return {"deleted_count": 1}