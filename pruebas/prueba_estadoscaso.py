# pruebas/prueba_estadoscaso.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.estadoscaso_dao import EstadosCasoDAO
from modelos.estadoscaso_modelo import estadosCaso

cn             = Conexion()
estadosCasoDAO = EstadosCasoDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: ESTADOS CASO")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 estados de caso --")
estadosNuevos = [
    ("Pendiente Revisión", "Caso asignado pero sin iniciar revisión", False),
    ("En Validación",      "Verificando información del cliente",     False),
    ("Escalado",           "Caso enviado a nivel superior",           False),
    ("Rechazado",          "Caso no procede según políticas",         True),
    ("Reabierto",          "Caso cerrado que fue vuelto a abrir",     False),
]
for nomEstado, descripcion, esFinal in estadosNuevos:
    nuevo             = estadosCaso()
    nuevo.nomEstado   = nomEstado
    nuevo.descripcion = descripcion
    nuevo.esfinal     = esFinal
    nuevo.activo      = True
    estadosCasoDAO.InsertEstadoCaso(nuevo)
    print("Estado insertado: " + nuevo.nomEstado + ", esFinal: " + str(nuevo.esfinal))

# --- SELECT todos ---
print("\n-- SELECT todos los estados de caso --")
listaEstados = estadosCasoDAO.SelectEstadosCaso()
for ec in listaEstados:
    print(str(ec.idEstado) + ", " + ec.nomEstado + ", " + ec.descripcion + ", " + str(ec.esfinal) + ", " + str(ec.activo))

# --- SELECT por ID ---
print("\n-- SELECT estado con id=1 --")
ec = estadosCasoDAO.SelectEstadoCasoId(1)
if ec:
    print(str(ec.idEstado) + ", " + ec.nomEstado + ", " + str(ec.esfinal))

# --- UPDATE ---
print("\n-- UPDATE estado con id=1 --")
actualizar             = estadosCaso()
actualizar.idEstado    = 1
actualizar.nomEstado   = "Abierto Actualizado"
actualizar.descripcion = "Caso recién creado y verificado"
actualizar.esfinal     = False
actualizar.activo      = True
estadosCasoDAO.UpdateEstadoCaso(actualizar)
print("Estado actualizado: " + str(actualizar.idEstado) + ", " + actualizar.nomEstado)

# --- DELETE ---
print("\n-- DELETE estado con id=9 --")
estadosCasoDAO.DeleteEstadoCaso(9)
print("Estado con id=9 eliminado correctamente")
