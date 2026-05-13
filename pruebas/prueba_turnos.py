# pruebas/prueba_turnos.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.turnos_dao import TurnosDAO
from modelos.turnos_modelo import Turnos

cn        = Conexion()
turnosDAO = TurnosDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: TURNOS")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 turnos --")
turnosNuevos = [
    ("Madrugada", "00:00:00", "08:00:00"),
    ("Nocturno",  "22:00:00", "06:00:00"),
    ("Extendido", "06:00:00", "20:00:00"),
    ("Medio Día", "10:00:00", "18:00:00"),
    ("Rotativo",  "08:00:00", "16:00:00"),
]
for nomturno, horaInicio, horaFin in turnosNuevos:
    nuevo            = Turnos()
    nuevo.nomturno   = nomturno
    nuevo.horaInicio = horaInicio
    nuevo.horaFin    = horaFin
    nuevo.activo     = True
    turnosDAO.InsertTurno(nuevo)
    print("Turno insertado: " + nuevo.nomturno + ", " + str(nuevo.horaInicio) + " - " + str(nuevo.horaFin))

# --- SELECT todos ---
print("\n-- SELECT todos los turnos --")
listaTurnos = turnosDAO.SelectTurnos()
for turno in listaTurnos:
    print(str(turno.idTurno) + ", " + turno.nomturno + ", " +
          str(turno.horaInicio) + ", " + str(turno.horaFin) + ", " + str(turno.activo))

# --- SELECT por ID ---
print("\n-- SELECT turno con id=1 --")
turno = turnosDAO.SelectTurnoId(1)
if turno:
    print(str(turno.idTurno) + ", " + turno.nomturno + ", " + str(turno.horaInicio))

# --- UPDATE ---
print("\n-- UPDATE turno con id=1 --")
actualizar            = Turnos()
actualizar.idTurno    = 1
actualizar.nomturno   = "Mañana Actualizado"
actualizar.horaInicio = "06:30:00"
actualizar.horaFin    = "14:30:00"
actualizar.activo     = True
turnosDAO.UpdateTurno(actualizar)
print("Turno actualizado: " + str(actualizar.idTurno) + ", " + actualizar.nomturno)

# --- DELETE ---
print("\n-- DELETE turno con id=7 --")
turnosDAO.DeleteTurno(7)
print("Turno con id=7 eliminado correctamente")
