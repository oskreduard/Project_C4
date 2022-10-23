from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria
from Modelos.Materia import Materia
class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
    def index(self):
        return self.repositorioMateria.findAll()
    def create(self,infoMateria):
        nuevoMateria =Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)
    def show(self,id):
        laMateria=Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__
    def update(self,id,infoMateria):
        MateriaActual=Materia(self.repositorioMateria.findById(id))
        MateriaActual.nombre = infoMateria["nombre"]
        MateriaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(MateriaActual)
    def delete(self,id):
        return self.repositorioEstudiante.delete(id)