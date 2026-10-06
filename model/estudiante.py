from .persona import Persona
from .excepciones import DeudaMatriculaException

class Estudiante(Persona):
    def __init__(self, rut, nombre, apellido, deuda_matricula_pendiente=False):
        super().__init__(rut, nombre, apellido)
        self.__deuda_matricula_pendiente = deuda_matricula_pendiente
        self.__matriculas = []

    @property
    def deuda_matricula_pendiente(self):
        return self.__deuda_matricula_pendiente

    @deuda_matricula_pendiente.setter
    def deuda_matricula_pendiente(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("La deuda_matricula_pendiente debe ser booleana.")
        self.__deuda_matricula_pendiente = valor

    @property
    def matriculas(self):
        return list(self.__matriculas)

    def tiene_deuda_pendiente(self):
        return self.__deuda_matricula_pendiente

    def solicitar_matricula(self, matricula):
        if self.__deuda_matricula_pendiente:
            raise DeudaMatriculaException(
                "El estudiante mantiene una deuda de matrícula pendiente."
            )
        self.__matriculas.append(matricula)
        return True
