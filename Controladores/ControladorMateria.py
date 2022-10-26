from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Materia import Materia
from Modelos.Departamento import Departamento
class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()
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
        return self.repositorioMateria.delete(id)
    def delete_all(self):
        return self.repositorioMateria.deleteAll()

    """
    Relación departamento y materia
    """
    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)