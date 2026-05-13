from conexion.conexion import Conexion;
from modelos.cargos_modelo import (Cargos)

class CargosDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

    # ----------------------------------------------------------
    # CARGOS - SELECT todas
    # ----------------------------------------------------------
    def SelectCargos(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_cargos()}");

        listaCargos: list = [];
        for fila in cursor:
            cargo = Cargos();
            cargo.idCargo  = fila[0];
            cargo.nomCargo = fila[1];
            cargo.nivel    = fila[2];
            cargo.activo   = fila[3];
            listaCargos.append(cargo);

        cursor.close();
        con.close();
        return listaCargos;

    # ----------------------------------------------------------
    # CARGOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectCargoId(self, idCargo: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_cargo_id(?)}", idCargo);

        cargo = None;
        for fila in cursor:
            cargo = Cargos();
            cargo.idCargo  = fila[0];
            cargo.nomCargo = fila[1];
            cargo.nivel    = fila[2];
            cargo.activo   = fila[3];

        cursor.close();
        con.close();
        return cargo;

    # ----------------------------------------------------------
    # CARGOS - INSERT
    # ----------------------------------------------------------
    def InsertCargo(self, cargo: Cargos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_cargo(?, ?, ?)}",
            cargo.nomCargo,
            cargo.nivel,
            cargo.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CARGOS - UPDATE
    # ----------------------------------------------------------
    def UpdateCargo(self, cargo: Cargos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_cargo(?, ?, ?, ?)}",
            cargo.idCargo,
            cargo.nomCargo,
            cargo.nivel,
            cargo.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CARGOS - DELETE
    # ----------------------------------------------------------
    def DeleteCargo(self, idCargo: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_cargo(?)}", idCargo);
        con.commit();
        cursor.close();
        con.close();