from Modelos.Inscripcion import Inscripcion
class ControladorInscripcion():

    def __init__(self):
        print("Creando ControladorInscripcion")

    def index(self):
        print("Listar todos las Inscripciones")
        Inscripciones = {
            "_id": "1",
            "Inscripcion": "Uno",
        }
        return [Inscripciones]

    def create(self, infoInscripcion):
        print("Crear un Inscripcion")
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def show(self, id):
        print("Mostrando una Inscripcion con id ", id)
        laInscripcion = {
            "_id": id,
            "Inscripcion": "Uno",
        }
        return laInscripcion

    def update(self, id, infoInscripcion):
        print("Actualizando la Materia con id ", id)
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def delete(self, id):
        print("Elimiando la Materia con id ", id)
        return {"deleted_count": 1}