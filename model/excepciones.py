class PeriodoCerradoException(Exception):
    """Se intenta realizar una operación cuando el periodo académico está cerrado."""
    pass


class DeudaMatriculaException(Exception):
    """El estudiante no puede solicitar matrícula porque mantiene una deuda pendiente."""
    pass


class CupoElectivoException(Exception):
    """El electivo no puede inscribirse porque no tiene cupos disponibles."""
    pass
