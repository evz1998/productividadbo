# pruebas/prueba_evaluaciones.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.evaluaciones_dao import EvaluacionesDAO
from modelos.evaluaciones_modelo import Evaluaciones

cn              = Conexion()
evaluacionesDAO = EvaluacionesDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: EVALUACIONES")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 evaluaciones --")
evaluacionesNuevas = [
    (1, "2025-01", 90.0, 95.0, 120, 92.0),
    (2, "2025-01", 85.0, 88.0,  98, 86.5),
    (3, "2025-01", 78.0, 80.0, 110, 79.0),
    (4, "2025-01", 95.0, 97.0, 135, 96.0),
    (1, "2025-02", 88.0, 91.0, 125, 89.5),
]
for idAsesor, periodo, calidad, puntualidad, casosGestionados, nota in evaluacionesNuevas:
    nueva                   = Evaluaciones()
    nueva.idAsesor          = idAsesor
    nueva.periodo           = periodo
    nueva.calidad           = calidad
    nueva.puntualidad       = puntualidad
    nueva.casosGestionados  = casosGestionados
    nueva.nota              = nota
    nueva.fechaEvaluacion   = datetime.datetime.now()
    evaluacionesDAO.InsertEvaluacion(nueva)
    print("Evaluación insertada: asesor " + str(nueva.idAsesor) + ", periodo " + nueva.periodo + ", nota: " + str(nueva.nota))

# --- SELECT todas ---
print("\n-- SELECT todas las evaluaciones --")
listaEvaluaciones = evaluacionesDAO.SelectEvaluaciones()
for ev in listaEvaluaciones:
    print(str(ev.idEvaluacion) + ", asesor:" + str(ev.idAsesor) +
          ", periodo:" + ev.periodo + ", calidad:" + str(ev.calidad) +
          ", puntualidad:" + str(ev.puntualidad) +
          ", casos:" + str(ev.casosGestionados) + ", nota:" + str(ev.nota))

# --- SELECT por ID ---
print("\n-- SELECT evaluación con id=1 --")
ev = evaluacionesDAO.SelectEvaluacionId(1)
if ev:
    print(str(ev.idEvaluacion) + ", asesor:" + str(ev.idAsesor) + ", nota:" + str(ev.nota))

# --- UPDATE ---
print("\n-- UPDATE evaluación con id=1 --")
actualizar                  = Evaluaciones()
actualizar.idEvaluacion     = 1
actualizar.idAsesor         = 1
actualizar.periodo          = "2025-01"
actualizar.calidad          = 93.0
actualizar.puntualidad      = 96.0
actualizar.casosGestionados = 130
actualizar.nota             = 94.5
actualizar.fechaEvaluacion  = datetime.datetime.now()
evaluacionesDAO.UpdateEvaluacion(actualizar)
print("Evaluación actualizada: id=" + str(actualizar.idEvaluacion) + ", nueva nota=" + str(actualizar.nota))

# --- DELETE ---
print("\n-- DELETE evaluación con id=5 --")
evaluacionesDAO.DeleteEvaluacion(5)
print("Evaluación con id=5 eliminada correctamente")
