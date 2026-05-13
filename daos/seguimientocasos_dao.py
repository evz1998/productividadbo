from conexion.conexion import Conexion;
from modelos.seguimientocasos_modelo import (seguimientoCasos)

class SeguimientoCasosDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

    # ----------------------------------------------------------
    #   SEGUIMIENTOS CASOS - SELECT todas
    # ----------------------------------------------------------
    def SelectSeguimientos(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_seguimientos()}");

        listaSeguimientos: list = [];
        for fila in cursor:
            seguimiento = seguimientoCasos();
            seguimiento.idSeguimiento   = fila[0];
            seguimiento.idCaso          = fila[1];
            seguimiento.idAsesor        = fila[2];
            seguimiento.idEstado        = fila[3];
            seguimiento.nota            = fila[4];
            seguimiento.fecharegistro   = fila[5];
            listaSeguimientos.append(seguimiento);

        cursor.close();
        con.close();
        return listaSeguimientos;

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectSeguimientoId(self, idSeguimiento: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_seguimiento_id(?)}", idSeguimiento);

        seguimiento = None;
        for fila in cursor:
            seguimiento = seguimientoCasos();
            seguimiento.idSeguimiento   = fila[0];
            seguimiento.idCaso          = fila[1];
            seguimiento.idAsesor        = fila[2];
            seguimiento.idEstado        = fila[3];
            seguimiento.nota            = fila[4];
            seguimiento.fecharegistro   = fila[5];

        cursor.close();
        con.close();
        return seguimiento;

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - INSERT
    # ----------------------------------------------------------
    def InsertSeguimiento(self, seguimiento: seguimientoCasos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_seguimiento(?, ?, ?, ?, ?)}",
            seguimiento.idCaso,
            seguimiento.idAsesor,
            seguimiento.idEstado,
            seguimiento.nota,
            seguimiento.fecharegistro
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - UPDATE
    # ----------------------------------------------------------
    def UpdateSeguimiento(self, seguimiento: seguimientoCasos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_seguimiento(?, ?, ?, ?, ?, ?)}",
            seguimiento.idSeguimiento,
            seguimiento.idCaso,
            seguimiento.idAsesor,
            seguimiento.idEstado,
            seguimiento.nota,
            seguimiento.fecharegistro
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # SEGUIMIENTOS CASOS - DELETE
    # ----------------------------------------------------------
    def DeleteSeguimiento(self, idSeguimiento: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_seguimiento(?)}", idSeguimiento);
        con.commit();
        cursor.close();
        con.close();
