# Colegio Nueva Esperanza — Evaluación Sumativa N°2

Proyecto de Programación Orientada a Objeto Seguro (TI3V21).

## Ejecución
Desde la raíz del repositorio:

```bash
python main.py
```

## Estructura
- `model/`: clases del modelo, una clase por archivo.
- `model/excepciones.py`: excepciones propias.
- `main.py`: demostración de herencia, polimorfismo, validación, composición y excepciones.

> Antes de entregar, revisar que los nombres, atributos, reglas de negocio y ponderaciones coincidan exactamente con el diagrama UML validado por el docente.


## Reglas de negocio demostradas
1. Deuda de matrícula pendiente -> `DeudaMatriculaException`.
2. Electivo sin cupo -> `CupoElectivoException`.

Además, el modelo contempla que las notas no pueden modificarse cuando el periodo académico está cerrado -> `PeriodoCerradoException`.
