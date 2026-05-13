# pruebas/prueba_metasproductividad.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.metasproductividad_dao import MetasProductividadDAO
from modelos.metasproductividad_modelo import MetasProductividad

cn                    = Conexion()
metasProductividadDAO = MetasProductividadDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: METAS PRODUCTIVIDAD")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 metas de productividad --")
metasNuevas = [
    (1, 1, 15, "2025-01-01", "2025-06-30"),
    (2, 2, 10, "2025-01-01", "2025-12-31"),
    (3, 3, 20, "2025-03-01", "2025-09-30"),
    (4, 4,  8, "2025-01-01", "2025-12-31"),
    (5, 5, 12, "2025-06-01", "2025-12-31"),
]
for idArea, idTipoCaso, casosMetaDia, vigDesde, vigHasta in metasNuevas:
    nueva               = MetasProductividad()
    nueva.idArea        = idArea
    nueva.idTipoCaso    = idTipoCaso
    nueva.casosMetaDia  = casosMetaDia
    nueva.vigenciaDesde = vigDesde
    nueva.vigenciaHasta = vigHasta
    nueva.activa        = True
    metasProductividadDAO.InsertMeta(nueva)
    print("Meta insertada: área " + str(nueva.idArea) + ", tipoCaso " + str(nueva.idTipoCaso) + ", meta/día: " + str(nueva.casosMetaDia))

# --- SELECT todas ---
print("\n-- SELECT todas las metas de productividad --")
listaMetas = metasProductividadDAO.SelectMetasProductividad()
for meta in listaMetas:
    print(str(meta.idMeta) + ", área:" + str(meta.idArea) + ", tipoCaso:" + str(meta.idTipoCaso) +
          ", metaDía:" + str(meta.casosMetaDia) + ", desde:" + str(meta.vigenciaDesde) +
          ", hasta:" + str(meta.vigenciaHasta) + ", activa:" + str(meta.activa))

# --- SELECT por ID ---
print("\n-- SELECT meta con id=1 --")
meta = metasProductividadDAO.SelectMetaProductividadId(1)
if meta:
    print(str(meta.idMeta) + ", área:" + str(meta.idArea) + ", meta/día:" + str(meta.casosMetaDia) + ", activa:" + str(meta.activa))

# --- UPDATE ---
print("\n-- UPDATE meta con id=1 --")
actualizar               = MetasProductividad()
actualizar.idMeta        = 1
actualizar.idArea        = 1
actualizar.idTipoCaso    = 1
actualizar.casosMetaDia  = 18
actualizar.vigenciaDesde = "2025-01-01"
actualizar.vigenciaHasta = "2025-12-31"
actualizar.activa        = True
metasProductividadDAO.UpdateMetaProductividad(actualizar)
print("Meta actualizada: id=" + str(actualizar.idMeta) + ", nueva meta/día=" + str(actualizar.casosMetaDia))

# --- DELETE ---
print("\n-- DELETE meta con id=5 --")
metasProductividadDAO.DeleteMetaProductividad(5)
print("Meta con id=5 eliminada correctamente")
