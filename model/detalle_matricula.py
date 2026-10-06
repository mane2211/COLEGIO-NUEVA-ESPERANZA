class DetalleMatricula:
    # CAMBIO 4: antes recibia (asignatura, arancel) con el arancel como numero suelto.
    # Ahora recibe el valor en pesos ya calculado y la asignatura, como en el diagrama.
    def __init__(self, valor, asignatura):
        self.__valor = valor
        self.__asignatura = asignatura

    @property
    def valor(self):
        return self.__valor

    @property
    def asignatura(self):
        return self.__asignatura

    def calcular_subtotal(self):
        return self.__valor
