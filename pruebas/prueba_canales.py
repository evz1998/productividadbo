# pruebas/prueba_canales.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.canales_dao import CanalesDAO
from modelos.canales_modelo import Canales

cn        = Conexion()
canalesDAO = CanalesDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: CANALES")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 canales --")
canalesNuevos = [
    ("WhatsApp",      "Casos recibidos por mensajería WhatsApp Business"),
    ("Redes Sociales","Casos recibidos por Facebook o Instagram"),
    ("Presencial",    "Casos atendidos en punto físico"),
    ("App Móvil",     "Casos generados desde la aplicación móvil"),
    ("SMS",           "Casos notificados por mensaje de texto"),
]
for nomCanal, descripcion in canalesNuevos:
    nuevo             = Canales()
    nuevo.nomCanal    = nomCanal
    nuevo.descripcion = descripcion
    nuevo.activo      = True
    canalesDAO.InsertCanal(nuevo)
    print("Canal insertado: " + nuevo.nomCanal + ", " + nuevo.descripcion)

# --- SELECT todos ---
print("\n-- SELECT todos los canales --")
listaCanales = canalesDAO.SelectCanales()
for canal in listaCanales:
    print(str(canal.idCanal) + ", " + canal.nomCanal + ", " + canal.descripcion + ", " + str(canal.activo))

# --- SELECT por ID ---
print("\n-- SELECT canal con id=1 --")
canal = canalesDAO.SelectCanalId(1)
if canal:
    print(str(canal.idCanal) + ", " + canal.nomCanal + ", " + str(canal.activo))

# --- UPDATE ---
print("\n-- UPDATE canal con id=1 --")
actualizar             = Canales()
actualizar.idCanal     = 1
actualizar.nomCanal    = "Email Corporativo"
actualizar.descripcion = "Casos recibidos por correo corporativo oficial"
actualizar.activo      = True
canalesDAO.UpdateCanal(actualizar)
print("Canal actualizado: " + str(actualizar.idCanal) + ", " + actualizar.nomCanal)

# --- DELETE ---
print("\n-- DELETE canal con id=8 --")
canalesDAO.DeleteCanal(8)
print("Canal con id=8 eliminado correctamente")
