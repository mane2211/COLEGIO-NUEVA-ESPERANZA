from .empleado import Empleado

class Administrativo(Empleado):
    def __init__(self, rut, nombre, apellido, cargo="Administrativo"):
        super().__init__(rut, nombre, apellido, cargo)

    def matricular(self, estudiante, matricula):
        estudiante.solicitar_matricula(matricula)
        return True

    def cobrar(self, matricula):
        return matricula.calcular_monto_total()
