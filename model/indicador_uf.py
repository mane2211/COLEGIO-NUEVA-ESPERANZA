# CAMBIO 4: archivo NUEVO. Esta clase estaba en el diagrama y faltaba en el codigo.
class IndicadorUF:
    def __init__(self, fecha, valor):
        self.__fecha = fecha
        self.__valor = valor

    @property
    def fecha(self):
        return self.__fecha

    def obtener_valor(self):
        return self.__valor
