# pruebas/prueba_clientes.py
import sys
sys.path.insert(0, "C:\\xampp\\htdocs\\productividadbo")
import datetime
from conexion.conexion import Conexion
from daos.clientes_dao import ClientesDAO
from modelos.clientes_modelo import Clientes

cn          = Conexion()
clientesDAO = ClientesDAO(cn)

print("\n" + "="*60)
print("PRUEBAS TABLA: CLIENTES")
print("="*60)

# --- INSERT 5 ---
print("\n-- INSERT 5 clientes --")
clientesNuevos = [
    ("9001", "Roberto Suárez", "rsuarez@email.com", "3200001001"),
    ("9002", "Mónica Ríos",    "mrios@email.com",   "3200001002"),
    ("9003", "Felipe Torres",  "ftorres@email.com", "3200001003"),
    ("9004", "Claudia Nieto",  "cnieto@email.com",  "3200001004"),
    ("9005", "Samuel Reyes",   "sreyes@email.com",  "3200001005"),
]
for documento, nombre, email, telefono in clientesNuevos:
    nuevo               = Clientes()
    nuevo.documento     = documento
    nuevo.nombre        = nombre
    nuevo.email         = email
    nuevo.telefono      = telefono
    nuevo.fechaRegistro = datetime.datetime.now()
    nuevo.activo        = True
    clientesDAO.InsertCliente(nuevo)
    print("Cliente insertado: " + nuevo.documento + ", " + nuevo.nombre + ", " + nuevo.email)

# --- SELECT todos ---
print("\n-- SELECT todos los clientes --")
listaClientes = clientesDAO.SelectClientes()
for cliente in listaClientes:
    print(str(cliente.idCliente) + ", " + cliente.documento + ", " + cliente.nombre + ", " +
          cliente.email + ", " + cliente.telefono + ", " + str(cliente.activo))

# --- SELECT por ID ---
print("\n-- SELECT cliente con id=1 --")
cliente = clientesDAO.SelectClienteId(1)
if cliente:
    print(str(cliente.idCliente) + ", " + cliente.documento + ", " + cliente.nombre + ", " + str(cliente.activo))

# --- UPDATE ---
print("\n-- UPDATE cliente con id=1 --")
actualizar               = Clientes()
actualizar.idCliente     = 1
actualizar.documento     = "8001"
actualizar.nombre        = "Pedro Álvarez Actualizado"
actualizar.email         = "palvarez2@email.com"
actualizar.telefono      = "3109001099"
actualizar.fechaRegistro = datetime.datetime.now()
actualizar.activo        = True
clientesDAO.UpdateCliente(actualizar)
print("Cliente actualizado: " + str(actualizar.idCliente) + ", " + actualizar.nombre)

# --- DELETE ---
print("\n-- DELETE cliente con id=7 --")
clientesDAO.DeleteCliente(7)
print("Cliente con id=7 eliminado correctamente")
