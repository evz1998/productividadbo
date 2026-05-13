# pruebas/prueba_areas.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")

import datetime
from conexion.conexion import Conexion
from daos.areas_dao import AreasDAO
from modelos.areas_modelo import Areas

cn       = Conexion()
areasDAO = AreasDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: AREAS")
print("="*60)

# --- INSERT 5 áreas ---
print("\n-- INSERT 5 áreas --")
areasNuevas = [
    ("Tecnología",     "Soporte técnico y sistemas",            True),
    ("Jurídica",       "Gestión legal y compliance",            True),
    ("Talento Humano", "Selección y bienestar del personal",    True),
    ("Auditoría",      "Control interno y revisión de cuentas", True),
    ("Comercial",      "Ventas y atención postventa",           False),
]
for nomArea, descripcion, activa in areasNuevas:
    nueva             = Areas()
    nueva.nomArea     = nomArea
    nueva.descripcion = descripcion
    nueva.activa      = activa
    areasDAO.InsertArea(nueva)
    print("Área insertada: " + nueva.nomArea + ", " + nueva.descripcion + ", " + str(nueva.activa))

# --- SELECT todas ---
print("\n-- SELECT todas las áreas --")
listaArea = areasDAO.SelectAreas()
for area in listaArea:
    print(str(area.idArea) + ", " + area.nomArea + ", " + area.descripcion + ", " + str(area.activa))

# --- SELECT por ID ---
print("\n-- SELECT área con id=1 --")
area = areasDAO.SelectAreaId(1)
if area:
    print(str(area.idArea) + ", " + area.nomArea + ", " + area.descripcion + ", " + str(area.activa))

# --- UPDATE ---
print("\n-- UPDATE área con id=1 --")
actualizar             = Areas()
actualizar.idArea      = 1
actualizar.nomArea     = "Cartera Actualizada"
actualizar.descripcion = "Gestión de cobros, cartera vencida y recuperación"
actualizar.activa      = True
areasDAO.UpdateArea(actualizar)
print("Área actualizada: " + str(actualizar.idArea) + ", " + actualizar.nomArea + ", " + str(actualizar.activa))

# --- DELETE ---
print("\n-- DELETE área con id=9 --")
areasDAO.DeleteArea(9)
print("Área con id=9 eliminada correctamente")
