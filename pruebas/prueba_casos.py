# pruebas/prueba_casos.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.casos_dao import CasosDAO
from modelos.casos_modelo import Casos

cn       = Conexion()
casosDAO = CasosDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: CASOS")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 casos --")
casosNuevos = [
    (1, 1, 2, 1, 1, 1, "Cliente reporta cobro duplicado en extracto de enero"),
    (2, 3, 1, 3, 2, 2, "Actualización de datos personales y dirección"),
    (3, 4, 4, 2, 2, 3, "Cuenta bloqueada por actividad inusual detectada"),
    (1, 2, 3, 1, 1, 4, "Solicitud de devolución por pago en exceso"),
    (2, 5, 2, 4, 1, 1, "Ajuste de saldo por error en liquidación de producto"),
]
for idCliente, idTipoCaso, idPrioridad, idCanal, idEstado, idAsesor, descripcion in casosNuevos:
    nuevo              = Casos()
    nuevo.idCliente    = idCliente
    nuevo.idTipoCaso   = idTipoCaso
    nuevo.idPrioridad  = idPrioridad
    nuevo.idCanal      = idCanal
    nuevo.idEstado     = idEstado
    nuevo.idAsesor     = idAsesor
    nuevo.descripcion  = descripcion
    nuevo.fechaApertura = datetime.datetime.now()
    nuevo.fechaCierre  = None
    casosDAO.InsertCasos(nuevo)
    print("Caso insertado: cliente " + str(nuevo.idCliente) + ", asesor " + str(nuevo.idAsesor) + ", " + nuevo.descripcion[:40] + "...")

# --- SELECT todos ---
print("\n-- SELECT todos los casos --")
listaCasos = casosDAO.SelectCasos()
for caso in listaCasos:
    print(str(caso.idCaso) + ", cli:" + str(caso.idCliente) + ", tip:" + str(caso.idTipoCaso) +
          ", pri:" + str(caso.idPrioridad) + ", est:" + str(caso.idEstado) +
          ", ase:" + str(caso.idAsesor) + ", " + caso.descripcion[:30] + "...")

# --- SELECT por ID ---
print("\n-- SELECT caso con id=1 --")
caso = casosDAO.SelectCasosId(1)
if caso:
    print(str(caso.idCaso) + ", " + caso.descripcion + ", " + str(caso.fechaApertura))

# --- UPDATE ---
print("\n-- UPDATE caso con id=1 --")
actualizar              = Casos()
actualizar.idCaso       = 1
actualizar.idCliente    = 1
actualizar.idTipoCaso   = 1
actualizar.idPrioridad  = 3
actualizar.idCanal      = 1
actualizar.idEstado     = 2
actualizar.idAsesor     = 1
actualizar.descripcion  = "Cliente reclama cobro doble - EN PROCESO DE REVISIÓN"
actualizar.fechaApertura = datetime.datetime.now()
actualizar.fechaCierre  = None
casosDAO.UpdateCasos(actualizar)
print("Caso actualizado: id=" + str(actualizar.idCaso) + ", estado=" + str(actualizar.idEstado))

# --- DELETE ---
print("\n-- DELETE caso con id=7 --")
casosDAO.DeleteCasos(7)
print("Caso con id=7 eliminado correctamente")
