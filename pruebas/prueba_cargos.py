# pruebas/prueba_cargos.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
from conexion.conexion import Conexion
from daos.cargos_dao import CargosDAO
from modelos.cargos_modelo import Cargos

cn        = Conexion()
cargosDAO = CargosDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: CARGOS")
print("="*60)

# --- INSERT 5 cargos ---
print("\n-- INSERT 5 cargos --")
cargosNuevos = [
    ("Analista",        1),
    ("Especialista",    2),
    ("Líder de Equipo", 3),
    ("Jefe de Área",    4),
    ("Director",        5),
]
for nomCargo, nivel in cargosNuevos:
    nuevo          = Cargos()
    nuevo.nomCargo = nomCargo
    nuevo.nivel    = nivel
    nuevo.activo   = True
    cargosDAO.InsertCargo(nuevo)
    print("Cargo insertado: " + nuevo.nomCargo + ", nivel: " + str(nuevo.nivel))

# --- SELECT todos ---
print("\n-- SELECT todos los cargos --")
listaCargos = cargosDAO.SelectCargos()
for cargo in listaCargos:
    print(str(cargo.idCargo) + ", " + cargo.nomCargo + ", " + str(cargo.nivel) + ", " + str(cargo.activo))

# --- SELECT por ID ---
print("\n-- SELECT cargo con id=1 --")
cargo = cargosDAO.SelectCargoId(1)
if cargo:
    print(str(cargo.idCargo) + ", " + cargo.nomCargo + ", " + str(cargo.nivel) + ", " + str(cargo.activo))

# --- UPDATE ---
print("\n-- UPDATE cargo con id=1 --")
actualizar          = Cargos()
actualizar.idCargo  = 1
actualizar.nomCargo = "Asesor Junior Actualizado"
actualizar.nivel    = 1
actualizar.activo   = True
cargosDAO.UpdateCargo(actualizar)
print("Cargo actualizado: " + str(actualizar.idCargo) + ", " + actualizar.nomCargo + ", " + str(actualizar.nivel))

# --- DELETE ---
print("\n-- DELETE cargo con id=8 --")
cargosDAO.DeleteCargo(8)
print("Cargo con id=8 eliminado correctamente")
