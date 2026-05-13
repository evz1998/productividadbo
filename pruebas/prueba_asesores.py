# pruebas/prueba_asesores.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.asesores_dao import AsesoresDAO
from modelos.asesores_modelo import Asesores

cn          = Conexion()
asesoresDAO = AsesoresDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: ASESORES")
print("="*60)

# --- INSERT 5 asesores ---
print("\n-- INSERT 5 asesores --")
asesoresNuevos = [
    ("20111001", "Juan Pérez",   "jperez@bo.com",    "3011110001", 1, 1),
    ("20111002", "Ana Martínez", "amartinez@bo.com", "3011110002", 2, 2),
    ("20111003", "Luis Herrera", "lherrera@bo.com",  "3011110003", 3, 1),
    ("20111004", "Sara Ospina",  "sospina@bo.com",   "3011110004", 4, 3),
    ("20111005", "Diego Vargas", "dvargas@bo.com",   "3011110005", 5, 2),
]
for cedula, nombre, email, telefono, idArea, idCargo in asesoresNuevos:
    nuevo              = Asesores()
    nuevo.cedula       = cedula
    nuevo.nombre       = nombre
    nuevo.email        = email
    nuevo.telefono     = telefono
    nuevo.idArea       = idArea
    nuevo.idCargo      = idCargo
    nuevo.fechaIngreso = datetime.datetime.now()
    nuevo.activo       = True
    asesoresDAO.InsertAsesor(nuevo)
    print("Asesor insertado: " + nuevo.cedula + ", " + nuevo.nombre + ", " + nuevo.email)

# --- SELECT todos ---
print("\n-- SELECT todos los asesores --")
listaAsesores = asesoresDAO.SelectAsesores()
for asesor in listaAsesores:
    print(str(asesor.idAsesor) + ", " + asesor.cedula + ", " + asesor.nombre + ", " +
          asesor.email + ", " + asesor.telefono + ", " +
          str(asesor.idArea) + ", " + str(asesor.idCargo) + ", " + str(asesor.activo))

# --- SELECT por ID ---
print("\n-- SELECT asesor con id=1 --")
asesor = asesoresDAO.SelectAsesorId(1)
if asesor:
    print(str(asesor.idAsesor) + ", " + asesor.cedula + ", " + asesor.nombre + ", " + str(asesor.activo))

# --- UPDATE ---
print("\n-- UPDATE asesor con id=1 --")
actualizar              = Asesores()
actualizar.idAsesor     = 1
actualizar.cedula       = "10425601"
actualizar.nombre       = "Laura Gómez Actualizada"
actualizar.email        = "lgomez2@backoffice.com"
actualizar.telefono     = "3001234599"
actualizar.idArea       = 1
actualizar.idCargo      = 2
actualizar.fechaIngreso = datetime.datetime.now()
actualizar.activo       = True
asesoresDAO.UpdateAsesor(actualizar)
print("Asesor actualizado: " + str(actualizar.idAsesor) + ", " + actualizar.nombre)

# --- DELETE ---
print("\n-- DELETE asesor con id=8 --")
asesoresDAO.DeleteAsesor(8)
print("Asesor con id=8 eliminado correctamente")
