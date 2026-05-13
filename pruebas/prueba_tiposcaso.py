# pruebas/prueba_tiposcaso.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.tiposcaso_dao import TiposCasoDAO
from modelos.tiposcaso_modelo import TiposCaso

cn           = Conexion()
tiposCasoDAO = TiposCasoDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: TIPOS CASO")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 tipos de caso --")
tiposNuevos = [
    ("Queja",             "Inconformidad general del cliente",          45),
    ("Reembolso",         "Devolución de dinero por error en cobro",   120),
    ("Asesoría",          "Consulta o acompañamiento al cliente",       30),
    ("Incidente Técnico", "Fallo en plataforma o sistema del cliente",  90),
    ("Cancelación",       "Solicitud de cancelación de producto",      150),
]
for nomTipo, descripcion, tiempoMeta in tiposNuevos:
    nuevo             = TiposCaso()
    nuevo.nomTipo     = nomTipo
    nuevo.descripcion = descripcion
    nuevo.tiempoMeta  = tiempoMeta
    nuevo.activo      = True
    tiposCasoDAO.InsertTipoCaso(nuevo)
    print("Tipo caso insertado: " + nuevo.nomTipo + ", meta: " + str(nuevo.tiempoMeta) + " min")

# --- SELECT todos ---
print("\n-- SELECT todos los tipos de caso --")
listaTiposCaso = tiposCasoDAO.SelectTiposCaso()
for tc in listaTiposCaso:
    print(str(tc.idTipoCaso) + ", " + tc.nomTipo + ", " + tc.descripcion + ", " + str(tc.tiempoMeta) + ", " + str(tc.activo))

# --- SELECT por ID ---
print("\n-- SELECT tipo caso con id=1 --")
tc = tiposCasoDAO.SelectTiposCasoId(1)
if tc:
    print(str(tc.idTipoCaso) + ", " + tc.nomTipo + ", " + str(tc.tiempoMeta))

# --- UPDATE ---
print("\n-- UPDATE tipo caso con id=1 --")
actualizar             = TiposCaso()
actualizar.idTipoCaso  = 1
actualizar.nomTipo     = "Reclamo Factura Actualizado"
actualizar.descripcion = "Inconformidad con el valor facturado - revisado"
actualizar.tiempoMeta  = 100
actualizar.activo      = True
tiposCasoDAO.UpdateTipoCaso(actualizar)
print("Tipo caso actualizado: " + str(actualizar.idTipoCaso) + ", " + actualizar.nomTipo)

# --- DELETE ---
print("\n-- DELETE tipo caso con id=11 --")
tiposCasoDAO.DeleteTipoCaso(11)
print("Tipo caso con id=11 eliminado correctamente")
