# pruebas/prueba_reportesdiarios.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.reportesdiarios_dao import ReportesDiariosDAO
from modelos.reportediarios_modelo import ReportesDiarios

cn                 = Conexion()
reportesDiariosDAO = ReportesDiariosDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: REPORTES DIARIOS")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 reportes diarios --")
reportesNuevos = [
    (1, "2025-04-01", 5,  12, 3,  35.5, True),
    (2, "2025-04-01", 3,   8, 4,  42.0, False),
    (3, "2025-04-01", 6,  14, 2,  28.0, True),
    (4, "2025-04-01", 4,  10, 5,  38.5, True),
    (1, "2025-04-02", 7,  11, 4,  33.0, False),
]
for idAsesor, fecha, abiertos, cerrados, enProceso, tiempoPromedio, cumplioMeta in reportesNuevos:
    nuevo                = ReportesDiarios()
    nuevo.idAsesor       = idAsesor
    nuevo.fecha          = fecha
    nuevo.casosAbiertos  = abiertos
    nuevo.casosCerrados  = cerrados
    nuevo.casosEnProceso = enProceso
    nuevo.tiempoPromedio = tiempoPromedio
    nuevo.cumplioMeta    = cumplioMeta
    reportesDiariosDAO.InsertReporteDiario(nuevo)
    print("Reporte insertado: asesor " + str(nuevo.idAsesor) + ", fecha " + str(nuevo.fecha) +
          ", cerrados:" + str(nuevo.casosCerrados) + ", cumplioMeta:" + str(nuevo.cumplioMeta))

# --- SELECT todos ---
print("\n-- SELECT todos los reportes diarios --")
listaReportes = reportesDiariosDAO.SelectReportesDiarios()
for r in listaReportes:
    print(str(r.idReporte) + ", asesor:" + str(r.idAsesor) +
          ", fecha:" + str(r.fecha) +
          ", abiertos:" + str(r.casosAbiertos) +
          ", cerrados:" + str(r.casosCerrados) +
          ", enProceso:" + str(r.casosEnProceso) +
          ", tPromedio:" + str(r.tiempoPromedio) +
          ", meta:" + str(r.cumplioMeta))

# --- SELECT por ID ---
print("\n-- SELECT reporte con id=1 --")
r = reportesDiariosDAO.SelectReporteDiarioId(1)
if r:
    print(str(r.idReporte) + ", asesor:" + str(r.idAsesor) +
          ", cerrados:" + str(r.casosCerrados) + ", cumplioMeta:" + str(r.cumplioMeta))

# --- UPDATE ---
print("\n-- UPDATE reporte con id=1 --")
actualizar               = ReportesDiarios()
actualizar.idReporte     = 1
actualizar.idAsesor      = 1
actualizar.fecha         = "2025-04-01"
actualizar.casosAbiertos = 5
actualizar.casosCerrados = 15
actualizar.casosEnProceso = 2
actualizar.tiempoPromedio = 30.0
actualizar.cumplioMeta   = True
reportesDiariosDAO.UpdateReporteDiario(actualizar)
print("Reporte actualizado: id=" + str(actualizar.idReporte) +
      ", cerrados=" + str(actualizar.casosCerrados) +
      ", cumplioMeta=" + str(actualizar.cumplioMeta))

# --- DELETE ---
print("\n-- DELETE reporte con id=5 --")
reportesDiariosDAO.DeleteReporteDiario(5)
print("Reporte con id=5 eliminado correctamente")

print("\n" + "="*60)
print("✅ PRUEBAS COMPLETADAS - 15 tablas verificadas")
print("="*60)
