from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento
class ControladorDepartamento():
    def __init__(self):
        print("Ingreso Controlador Departamento")
        self.repositorioDepartamento = RepositorioDepartamento()
    def index(self):
        return self.repositorioDepartamento.findAll()
    def create(self,infoDepartamento):
        nuevoDepartamento=Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)
    def show(self,id):
        elDepartamento=Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__
    def update(self,id,infoDepartamento):
        DepartamentoActual=Departamento(self.repositorioDepartamento.findById(id))
        DepartamentoActual.nombre = infoDepartamento["nombre"]
        return self.repositorioDepartamento.save(DepartamentoActual)
    def delete(self,id):
        return self.repositorioDepartamento.delete(id)
    def delete_all(self):
        return self.repositorioDepartamento.deleteAll()