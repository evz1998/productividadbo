# pruebas/prueba_seguimientocasos.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.seguimientocasos_dao import SeguimientoCasosDAO
from modelos.seguimientocasos_modelo import seguimientoCasos

cn                  = Conexion()
seguimientoCasosDAO = SeguimientoCasosDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: SEGUIMIENTOS CASO")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 seguimientos --")
seguimientosNuevos = [
    (1, 1, 2, "Caso revisado, se solicita extracto al cliente"),
    (1, 2, 3, "Extracto recibido, en validación con el área de facturación"),
    (2, 2, 1, "Datos actualizados en sistema exitosamente"),
    (3, 3, 4, "Cuenta desbloqueada previa validación de identidad"),
    (4, 1, 2, "Devolución aprobada, pendiente procesamiento en tesorería"),
]
for idCaso, idAsesor, idEstado, nota in seguimientosNuevos:
    nuevo               = seguimientoCasos()
    nuevo.idCaso        = idCaso
    nuevo.idAsesor      = idAsesor
    nuevo.idEstado      = idEstado
    nuevo.nota          = nota
    nuevo.fecharegistro = datetime.datetime.now()
    seguimientoCasosDAO.InsertSeguimiento(nuevo)
    print("Seguimiento insertado: caso " + str(nuevo.idCaso) + ", asesor " + str(nuevo.idAsesor) + ", " + nuevo.nota[:40] + "...")

# --- SELECT todos ---
print("\n-- SELECT todos los seguimientos --")
listaSeguimientos = seguimientoCasosDAO.SelectSeguimientos()
for seg in listaSeguimientos:
    print(str(seg.idSeguimiento) + ", caso:" + str(seg.idCaso) + ", asesor:" + str(seg.idAsesor) +
          ", estado:" + str(seg.idEstado) + ", " + seg.nota[:35] + "...")

# --- SELECT por ID ---
print("\n-- SELECT seguimiento con id=1 --")
seg = seguimientoCasosDAO.SelectSeguimientoId(1)
if seg:
    print(str(seg.idSeguimiento) + ", " + seg.nota + ", " + str(seg.fecharegistro))

# --- UPDATE ---
print("\n-- UPDATE seguimiento con id=1 --")
actualizar                = seguimientoCasos()
actualizar.idSeguimiento  = 1
actualizar.idCaso         = 1
actualizar.idAsesor       = 1
actualizar.idEstado       = 3
actualizar.nota           = "Caso revisado y escalado a coordinación para aprobación"
actualizar.fecharegistro  = datetime.datetime.now()
seguimientoCasosDAO.UpdateSeguimiento(actualizar)
print("Seguimiento actualizado: id=" + str(actualizar.idSeguimiento) + ", " + actualizar.nota[:40] + "...")

# --- DELETE ---
print("\n-- DELETE seguimiento con id=5 --")
seguimientoCasosDAO.DeleteSeguimiento(5)
print("Seguimiento con id=5 eliminado correctamente")
