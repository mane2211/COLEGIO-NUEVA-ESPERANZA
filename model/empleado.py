from .persona import Persona

class Empleado(Persona):
    def __init__(self, rut, nombre, apellido, cargo):
        super().__init__(rut, nombre, apellido)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    def registrar_accion(self):
        return f"{self.nombre} registró una acción como {self.__cargo}."
