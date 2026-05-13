from conexion.conexion import Conexion;
from modelos.estadoscaso_modelo import (estadosCaso)

class EstadosCasoDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

    # ----------------------------------------------------------
    # ESTADOS CASO - SELECT todas
    # ----------------------------------------------------------
    def SelectEstadosCaso(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_estadosCaso()}");

        listaEstadosCaso: list = [];
        for fila in cursor:
            estadocaso = estadosCaso();
            estadocaso.idEstado    = fila[0];
            estadocaso.nomEstado   = fila[1];
            estadocaso.descripcion = fila[2];
            estadocaso.esfinal     = fila[3];
            estadocaso.activo      = fila[4];
            listaEstadosCaso.append(estadocaso);

        cursor.close();
        con.close();
        return listaEstadosCaso;

    # ----------------------------------------------------------
    # ESTADOS CASO - SELECT por ID
    # ----------------------------------------------------------
    def SelectEstadoCasoId(self, idEstadoCaso: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_estadoCaso_id(?)}", idEstadoCaso);

        estadocaso = None;
        for fila in cursor:
            estadocaso = estadosCaso();
            estadocaso.idEstado    = fila[0];
            estadocaso.nomEstado   = fila[1];
            estadocaso.descripcion = fila[2];
            estadocaso.esfinal     = fila[3];
            estadocaso.activo      = fila[4];

        cursor.close();
        con.close();
        return estadocaso;

    # ----------------------------------------------------------
    # ESTADOS CASO - INSERT
    # ----------------------------------------------------------
    def InsertEstadoCaso(self, estadocaso: estadosCaso) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_estadoCaso(?, ?, ?, ?)}",
            estadocaso.nomEstado,
            estadocaso.descripcion,
            estadocaso.esfinal,
            estadocaso.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # ESTADOS CASO - UPDATE
    # ----------------------------------------------------------
    def UpdateEstadoCaso(self, estadocaso: estadosCaso) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_estadoCaso(?, ?, ?, ?, ?)}",
            estadocaso.idEstado,
            estadocaso.nomEstado,
            estadocaso.descripcion,
            estadocaso.esfinal,
            estadocaso.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # ESTADOS CASO - DELETE
    # ----------------------------------------------------------
    def DeleteEstadoCaso(self, idEstadoCaso: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_estadoCaso(?)}", idEstadoCaso);
        con.commit();
        cursor.close();
        con.close();
