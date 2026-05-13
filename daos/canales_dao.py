from conexion.conexion import Conexion;
from modelos.canales_modelo import (Canales)

class CanalesDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;


    # ----------------------------------------------------------
    # CANALES - SELECT todas
    # ----------------------------------------------------------
    def SelectCanales(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_canales()}");

        listaCanales: list = [];
        for fila in cursor:
            canal = Canales();
            canal.idCanal     = fila[0];
            canal.nomCanal    = fila[1];
            canal.descripcion = fila[2];
            canal.activo      = fila[3];
            listaCanales.append(canal);

        cursor.close();
        con.close();
        return listaCanales;

    # ----------------------------------------------------------
    # CANALES - SELECT por ID
    # ----------------------------------------------------------
    def SelectCanalId(self, idCanal: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_canal_id(?)}", idCanal);

        canal = None;
        for fila in cursor:
            canal = Canales();
            canal.idCanal     = fila[0];
            canal.nomCanal    = fila[1];
            canal.descripcion = fila[2];
            canal.activo      = fila[3];

        cursor.close();
        con.close();
        return canal;

    # ----------------------------------------------------------
    # CANALES - INSERT
    # ----------------------------------------------------------
    def InsertCanal(self, canal: Canales) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_canal(?, ?, ?)}",
            canal.nomCanal,
            canal.descripcion,
            canal.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CANALES - UPDATE
    # ----------------------------------------------------------
    def UpdateCanal(self, canal: Canales) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_canal(?, ?, ?, ?)}",
            canal.idCanal,
            canal.nomCanal,
            canal.descripcion,
            canal.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CANALES - DELETE
    # ----------------------------------------------------------
    def DeleteCanal(self, idCanal: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_canal(?)}", idCanal);
        con.commit();
        cursor.close();
        con.close();