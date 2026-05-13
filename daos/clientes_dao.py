from conexion.conexion import Conexion;
from conexion.encriptacion import encriptar, desencriptar;
from modelos.clientes_modelo import (Clientes)

class ClientesDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;


    # ----------------------------------------------------------
    # CLIENTES - SELECT todas
    # ----------------------------------------------------------
    def SelectClientes(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_clientes()}");

        listaClientes: list = [];
        for fila in cursor:
            cliente = Clientes();
            cliente.idCliente     = fila[0];
            cliente.documento     = desencriptar(fila[1]);
            cliente.nombre        = desencriptar(fila[2]);
            cliente.email         = desencriptar(fila[3]);
            cliente.telefono      = desencriptar(fila[4]);
            cliente.fechaRegistro = fila[5];
            cliente.activo        = fila[6];
            listaClientes.append(cliente);

        cursor.close();
        con.close();
        return listaClientes;

    # ----------------------------------------------------------
    # CLIENTES - SELECT por ID
    # ----------------------------------------------------------
    def SelectClienteId(self, idCliente: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_cliente_id(?)}", idCliente);

        cliente = None;
        for fila in cursor:
            cliente = Clientes();
            cliente.idCliente     = fila[0];
            cliente.documento     = desencriptar(fila[1]);
            cliente.nombre        = desencriptar(fila[2]);
            cliente.email         = desencriptar(fila[3]);
            cliente.telefono      = desencriptar(fila[4]);
            cliente.fechaRegistro = fila[5];
            cliente.activo        = fila[6];

        cursor.close();
        con.close();
        return cliente;

    # ----------------------------------------------------------
    # CLIENTES - INSERT
    # ----------------------------------------------------------
    def InsertCliente(self, cliente: Clientes) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_cliente(?, ?, ?, ?, ?, ?)}",
            encriptar(cliente.documento),
            encriptar(cliente.nombre),
            encriptar(cliente.email),
            encriptar(cliente.telefono),
            cliente.fechaRegistro,
            cliente.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CLIENTES - UPDATE
    # ----------------------------------------------------------
    def UpdateCliente(self, cliente: Clientes) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_cliente(?, ?, ?, ?, ?, ?, ?)}",
            cliente.idCliente,
            encriptar(cliente.documento),
            encriptar(cliente.nombre),
            encriptar(cliente.email),
            encriptar(cliente.telefono),
            cliente.fechaRegistro,
            cliente.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CLIENTES - DELETE
    # ----------------------------------------------------------
    def DeleteCliente(self, idCliente: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_cliente(?)}", idCliente);
        con.commit();
        cursor.close();
        con.close();