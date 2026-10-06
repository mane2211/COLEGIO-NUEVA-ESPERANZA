class Asignatura:
    def __init__(self, codigo, nombre, cupo, es_electivo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cupo = cupo
        self.__es_electivo = es_electivo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cupo(self):
        return self.__cupo

    @cupo.setter
    def cupo(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El cupo debe ser un entero mayor o igual a 0.")
        self.__cupo = valor

    @property
    def es_electivo(self):
        return self.__es_electivo

    def tiene_cupo(self):
        return self.__cupo > 0
