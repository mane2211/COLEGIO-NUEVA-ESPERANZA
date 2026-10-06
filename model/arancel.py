# CAMBIO 4: archivo NUEVO. Esta clase estaba en el diagrama y faltaba en el codigo.
class Arancel:
    def __init__(self, valor_uf):
        self.__valor_uf = valor_uf
        self.__valor_pesos = 0.0

    @property
    def valor_uf(self):
        return self.__valor_uf

    @property
    def valor_pesos(self):
        return self.__valor_pesos

    def calcular_valor_pesos(self, valor_uf_dia):
        self.__valor_pesos = self.__valor_uf * valor_uf_dia
        return self.__valor_pesos
