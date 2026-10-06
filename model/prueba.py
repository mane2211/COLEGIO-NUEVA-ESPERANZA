from .evaluacion import Evaluacion

class Prueba(Evaluacion):
    PONDERACION = 0.40

    # CAMBIO 1: antes no tenia constructor. La pauta pide que los subtipos
    # llamen a super().__init__() para reutilizar el constructor de Evaluacion.
    def __init__(self, fecha, nota, observacion, asignatura, profesor, periodo_academico):
        super().__init__(fecha, nota, observacion, asignatura, profesor, periodo_academico)

    def calcular_aporte(self):
        return self.nota * self.PONDERACION
