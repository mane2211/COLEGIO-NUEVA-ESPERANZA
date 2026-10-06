from abc import ABC, abstractmethod
# CAMBIO 5: import nuevo. Ahora la regla del periodo cerrado vive aqui.
from .excepciones import PeriodoCerradoException

class Evaluacion(ABC):
    def __init__(self, fecha, nota, observacion, asignatura, profesor, periodo_academico):
        self.__fecha = fecha
        # CAMBIO 2: antes era "self.__nota = nota", que se saltaba la validacion
        # del setter (se podia crear una prueba con nota 9.0). Ahora pasa por el setter.
        self.nota = nota
        self.__observacion = observacion
        self.__asignatura = asignatura
        self.__profesor = profesor
        self.__periodo_academico = periodo_academico

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if not isinstance(valor, (int, float)) or not 1.0 <= float(valor) <= 7.0:
            raise ValueError("La nota debe estar entre 1.0 y 7.0.")
        self.__nota = float(valor)

    @property
    def observacion(self):
        return self.__observacion

    @observacion.setter
    def observacion(self, valor):
        self.__observacion = valor

    @property
    def periodo_academico(self):
        return self.__periodo_academico

    def calcular_promedio(self):
        return self.__nota

    @abstractmethod
    def calcular_aporte(self):
        pass

    def editar_nota(self, nota):
        # CAMBIO 5: la regla "periodo cerrado" ahora se revisa aqui, en un solo lugar.
        # Antes solo estaba en Profesor.modificar_nota y ingresar_nota la esquivaba.
        if not self.__periodo_academico.esta_abierto():
            raise PeriodoCerradoException(
                "No se puede modificar la nota porque el periodo académico está cerrado."
            )
        self.nota = nota
        return True
