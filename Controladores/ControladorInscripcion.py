from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Modelos.Inscripcion import Inscripcion
class ControladorInscripcion():
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
    def index(self):
        return self.repositorioInscripcion.findAll()
    def create(self,infoInscripcion):
        nuevaInscripcion=Inscripcion(infoInscripcion)
        return self.repositorioInscripcion.save(nuevaInscripcion)
    def show(self,id):
        laInscripcion=Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__
    def update(self,id,infoInscripcion):
        InscripcionAcutal=Inscripcion(self.repositorioInscripcion.findById(id))
        InscripcionAcutal.anio=infoInscripcion["anio"]
        InscripcionAcutal.semestre = infoInscripcion["semestre"]
        InscripcionAcutal.nota_final = infoInscripcion["nota_final"]
        return self.repositorioInscripcion.save(estudianteActual)
    def delete(self,id):
        return self.repositorioEstudiante.delete(id)