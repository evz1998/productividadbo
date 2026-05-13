# pruebas/prueba_asistencia.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.asistencia_dao import AsistenciaDAO
from modelos.asistencia_modelo import Asistencia

cn            = Conexion()
asistenciaDAO = AsistenciaDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: ASISTENCIAS")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 asistencias --")
asistenciasNuevas = [
    (1, 1, 480),
    (2, 2, 450),
    (3, 1, 480),
    (4, 3, 360),
    (1, 2, 420),
]
for idAsesor, idTurno, minutos in asistenciasNuevas:
    nueva                   = Asistencia()
    nueva.idAsesor          = idAsesor
    nueva.idTurno           = idTurno
    nueva.fecha             = datetime.datetime.now()
    nueva.horaEntrada       = datetime.datetime.now()
    nueva.horaSalida        = datetime.datetime.now()
    nueva.minutosTrabajados = minutos
    asistenciaDAO.InsertAsistencia(nueva)
    print("Asistencia insertada: asesor " + str(nueva.idAsesor) + ", turno " + str(nueva.idTurno) + ", " + str(nueva.minutosTrabajados) + " min")

# --- SELECT todas ---
print("\n-- SELECT todas las asistencias --")
listaAsistencias = asistenciaDAO.SelectAsistencias()
for a in listaAsistencias:
    print(str(a.idAsistencia) + ", asesor:" + str(a.idAsesor) +
          ", turno:" + str(a.idTurno) + ", " + str(a.fecha) +
          ", mins:" + str(a.minutosTrabajados))

# --- SELECT por ID ---
print("\n-- SELECT asistencia con id=1 --")
a = asistenciaDAO.SelectAsistenciaId(1)
if a:
    print(str(a.idAsistencia) + ", asesor:" + str(a.idAsesor) + ", mins:" + str(a.minutosTrabajados))

# --- UPDATE ---
print("\n-- UPDATE asistencia con id=1 --")
actualizar                   = Asistencia()
actualizar.idAsistencia      = 1
actualizar.idAsesor          = 1
actualizar.idTurno           = 1
actualizar.fecha             = datetime.datetime.now()
actualizar.horaEntrada       = datetime.datetime.now()
actualizar.horaSalida        = datetime.datetime.now()
actualizar.minutosTrabajados = 500
asistenciaDAO.UpdateAsistencia(actualizar)
print("Asistencia actualizada: id=" + str(actualizar.idAsistencia) + ", mins=" + str(actualizar.minutosTrabajados))

# --- DELETE ---
print("\n-- DELETE asistencia con id=5 --")
asistenciaDAO.DeleteAsistencia(5)
print("Asistencia con id=5 eliminada correctamente")
