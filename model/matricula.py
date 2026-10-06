from .detalle_matricula import DetalleMatricula
from .excepciones import CupoElectivoException

class Matricula:
    # CAMBIO 4: antes recibia (estudiante, periodo_academico). Ahora tiene los
    # atributos que dibujaron en el diagrama: folio, fecha, monto, pago y UF aplicada.
    def __init__(self, folio, fecha_matricula):
        self.__folio = folio
        self.__fecha_matricula = fecha_matricula
        self.__monto_total = 0.0
        self.__pago_realizado = False
        self.__valor_uf_aplicado = 0.0
        self.__detalles = []  # composición: la matrícula crea y administra sus detalles
        self.__arancel = None  # agregación: la matrícula usa un Arancel existente

    @property
    def folio(self):
        return self.__folio

    @property
    def fecha_matricula(self):
        return self.__fecha_matricula

    @property
    def monto_total(self):
        return self.__monto_total

    @property
    def pago_realizado(self):
        return self.__pago_realizado

    @property
    def valor_uf_aplicado(self):
        return self.__valor_uf_aplicado

    @property
    def detalles(self):
        return list(self.__detalles)

    @property
    def arancel(self):
        return self.__arancel

    # CAMBIO 4: antes recibia (asignatura, arancel) con arancel como numero.
    # Ahora usa Arancel e IndicadorUF y CREA el detalle aqui dentro (composicion).
    def agregar_detalle(self, asignatura, arancel, indicador_uf):
        if asignatura.es_electivo and not asignatura.tiene_cupo():
            raise CupoElectivoException(
                f"El electivo {asignatura.nombre} no tiene cupos disponibles."
            )

        self.__arancel = arancel
        valor_uf = indicador_uf.obtener_valor()
        self.__valor_uf_aplicado = valor_uf
        valor_pesos = arancel.calcular_valor_pesos(valor_uf)
        detalle = DetalleMatricula(valor_pesos, asignatura)
        self.__detalles.append(detalle)
        if asignatura.tiene_cupo():
            asignatura.cupo -= 1
        self.calcular_monto_total()
        return detalle

    def calcular_monto_total(self):
        self.__monto_total = sum(detalle.calcular_subtotal() for detalle in self.__detalles)
        return self.__monto_total
