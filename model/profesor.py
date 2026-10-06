from .empleado import Empleado
# CAMBIO 5: se borro el import de PeriodoCerradoException, ya no se usa aqui
# (la excepcion ahora la lanza Evaluacion.editar_nota).

class Profesor(Empleado):
    def __init__(self, rut, nombre, apellido, cargo="Profesor"):
        super().__init__(rut, nombre, apellido, cargo)

    def ingresar_nota(self, evaluacion, nota):
        # CAMBIO 5: antes hacia "evaluacion.nota = nota" y no revisaba el periodo.
        evaluacion.editar_nota(nota)
        return True

    def ingresar_observacion(self, evaluacion, texto):
        evaluacion.observacion = texto
        return True

    def modificar_nota(self, evaluacion, nota):
        # CAMBIO 5: antes la revision del periodo estaba aqui; ahora esta en editar_nota.
        evaluacion.editar_nota(nota)
        return True
