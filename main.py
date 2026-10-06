from datetime import date

from model.asignatura import Asignatura
from model.periodo_academico import PeriodoAcademico
from model.profesor import Profesor
from model.prueba import Prueba
from model.trabajo import Trabajo
from model.presentacion_oral import PresentacionOral
from model.estudiante import Estudiante
from model.matricula import Matricula
# CAMBIO 4: imports nuevos de las dos clases que faltaban.
from model.arancel import Arancel
from model.indicador_uf import IndicadorUF
from model.excepciones import (
    PeriodoCerradoException,
    DeudaMatriculaException,
    CupoElectivoException,
)

print("=== COLEGIO NUEVA ESPERANZA ===")

# 1. Subtipos y polimorfismo
periodo = PeriodoAcademico(2026, 2, "abierto", date(2026, 12, 31))
asignatura = Asignatura("MAT101", "Matemática", 30, False)
# CAMBIO 3: el RUT de ejemplo era "12345678-9", que no es valido (el digito correcto es 5).
profesor = Profesor("12345678-5", "Ana", "Pérez")

evaluaciones = [
    Prueba(date.today(), 6.0, "Prueba 1", asignatura, profesor, periodo),
    Trabajo(date.today(), 5.5, "Trabajo 1", asignatura, profesor, periodo),
    PresentacionOral(date.today(), 6.5, "Presentación 1", asignatura, profesor, periodo),
]

print("\n1. SUBTIPOS Y POLIMORFISMO")
for evaluacion in evaluaciones:
    print(type(evaluacion).__name__,
          "-> calcular_aporte():",
          round(evaluacion.calcular_aporte(), 2))

# 2. Composición: matrícula + detalles
estudiante = Estudiante("11111111-1", "Mariana", "Puglicivich")
# CAMBIO 4: ahora la matricula usa folio y fecha, y el valor sale de Arancel + IndicadorUF.
indicador_uf = IndicadorUF(date.today(), 39000.0)
arancel = Arancel(2.5)
matricula = Matricula(1001, date.today())
matricula.agregar_detalle(asignatura, arancel, indicador_uf)
matricula.agregar_detalle(
    Asignatura("HIS101", "Historia", 25, True), arancel, indicador_uf
)

print("\n2. MATRÍCULA Y DETALLES")
print("Cantidad de detalles:", len(matricula.detalles))
print("Monto total:", matricula.calcular_monto_total())

# 3. Validación mediante property/setter
print("\n3. VALIDACIÓN CON PROPERTY Y SETTER")
try:
    evaluaciones[0].nota = 9.0
except ValueError as error:
    print("Validación capturada (nota):", error)

# CAMBIO 2: antes una nota de 9.0 se aceptaba al CREAR la evaluacion.
try:
    Prueba(date.today(), 9.0, "Prueba inválida", asignatura, profesor, periodo)
except ValueError as error:
    print("Validación capturada (nota al crear):", error)

# CAMBIO 3: nueva validacion del RUT.
try:
    Estudiante("12345678-9", "Pedro", "Mora")
except ValueError as error:
    print("Validación capturada (RUT):", error)

# 4. Primera regla: periodo cerrado
print("\n4. REGLAS DE NEGOCIO Y EXCEPCIONES")
periodo.estado = "cerrado"
try:
    profesor.modificar_nota(evaluaciones[0], 6.5)
except PeriodoCerradoException as error:
    print("PeriodoCerradoException capturada (modificar_nota):", error)

# CAMBIO 5: antes ingresar_nota esquivaba la regla; ahora tambien se bloquea.
try:
    profesor.ingresar_nota(evaluaciones[1], 6.0)
except PeriodoCerradoException as error:
    print("PeriodoCerradoException capturada (ingresar_nota):", error)

# 5. Segunda regla: electivo sin cupo
electivo_sin_cupo = Asignatura("ING201", "Inglés Electivo", 0, True)
matricula_electivo = Matricula(1003, date.today())
try:
    matricula_electivo.agregar_detalle(electivo_sin_cupo, arancel, indicador_uf)
except CupoElectivoException as error:
    print("CupoElectivoException capturada:", error)

# 6. Tercera regla adicional del modelo: deuda de matrícula
estudiante_con_deuda = Estudiante(
    "22222222-2", "Debora", "Toledo", deuda_matricula_pendiente=True
)
# CAMBIO 4: la matricula ahora se crea con folio y fecha.
matricula_deuda = Matricula(1002, date.today())
try:
    estudiante_con_deuda.solicitar_matricula(matricula_deuda)
except DeudaMatriculaException as error:
    print("DeudaMatriculaException capturada:", error)

print("\nPrograma finalizado correctamente.")
