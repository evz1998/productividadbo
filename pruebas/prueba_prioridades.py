# pruebas/prueba_prioridades.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.prioridades_dao import PrioridadesDAO
from modelos.prioridades_modelo import Prioridades

cn             = Conexion()
prioridadesDAO = PrioridadesDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: PRIORIDADES")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 prioridades --")
prioridadesNuevas = [
    ("Muy Baja",   0),
    ("Programada", 1),
    ("Normal",     2),
    ("Urgente",    3),
    ("Inmediata",  5),
]
for nomPrioridad, nivel in prioridadesNuevas:
    nueva              = Prioridades()
    nueva.nomPrioridad = nomPrioridad
    nueva.nivel        = nivel
    nueva.activa       = True
    prioridadesDAO.InsertPrioridad(nueva)
    print("Prioridad insertada: " + nueva.nomPrioridad + ", nivel: " + str(nueva.nivel))

# --- SELECT todas ---
print("\n-- SELECT todas las prioridades --")
listaPrioridades = prioridadesDAO.SelectPrioridades()
for p in listaPrioridades:
    print(str(p.idPrioridad) + ", " + p.nomPrioridad + ", " + str(p.nivel) + ", " + str(p.activa))

# --- SELECT por ID ---
print("\n-- SELECT prioridad con id=1 --")
p = prioridadesDAO.SelectPrioridadId(1)
if p:
    print(str(p.idPrioridad) + ", " + p.nomPrioridad + ", " + str(p.nivel))

# --- UPDATE ---
print("\n-- UPDATE prioridad con id=1 --")
actualizar              = Prioridades()
actualizar.idPrioridad  = 1
actualizar.nomPrioridad = "Baja Actualizada"
actualizar.nivel        = 1
actualizar.activa       = True
prioridadesDAO.UpdatePrioridad(actualizar)
print("Prioridad actualizada: " + str(actualizar.idPrioridad) + ", " + actualizar.nomPrioridad)

# --- DELETE ---
print("\n-- DELETE prioridad con id=8 --")
prioridadesDAO.DeletePrioridad(8)
print("Prioridad con id=8 eliminada correctamente")
