from Modelos.Materia import Materia
class ControladorMateria():

    def __init__(self):
        print("Creando ControladorMateria")

    def index(self):
        print("Listar todos las Materias")
        Materias = {
            "_id": "1",
            "Materia": "Calculo I",
        }
        return [Materias]

    def create(self, infoMateria):
        print("Crear un Materia")
        laMateria = Materia(infoMateria)
        return laMateria.__dict__

    def show(self, id):
        print("Mostrando una Materia con id ", id)
        laMateria = {
            "_id": id,
            "Materia": "Calculo I",
        }
        return laMateria

    def update(self, id, infoMateria):
        print("Actualizando la Materia con id ", id)
        laMateria = Materia(infoMateria)
        return laMateria.__dict__

    def delete(self, id):
        print("Elimiando la Materia con id ", id)
        return {"deleted_count": 1}