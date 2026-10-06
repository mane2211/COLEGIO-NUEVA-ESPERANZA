from datetime import date

class PeriodoAcademico:
    def __init__(self, anio, semestre, estado, fecha_cierre):
        self.__anio = anio
        self.__semestre = semestre
        self.__estado = estado
        self.__fecha_cierre = fecha_cierre

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El estado no puede estar vacío.")
        self.__estado = valor

    def esta_abierto(self):
        return self.__estado.lower() == "abierto"
