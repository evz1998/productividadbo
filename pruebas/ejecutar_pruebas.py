# pruebas/ejecutar_pruebas.py

import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")

# ============================================================
# Tablas maestras primero
# ============================================================
import pruebas.prueba_areas
import pruebas.prueba_cargos
import pruebas.prueba_tiposcaso
import pruebas.prueba_prioridades
import pruebas.prueba_estadoscaso
import pruebas.prueba_canales
import pruebas.prueba_turnos

# ============================================================
# Tablas que dependen de las anteriores
# ============================================================
import pruebas.prueba_asesores
import pruebas.prueba_clientes

# ============================================================
# Tablas que dependen de asesores y clientes
# ============================================================
import pruebas.prueba_casos
import pruebas.prueba_seguimientocasos
import pruebas.prueba_asistencia
import pruebas.prueba_metasproductividad
import pruebas.prueba_evaluaciones
import pruebas.prueba_reportesdiarios