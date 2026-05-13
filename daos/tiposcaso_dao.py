from conexion.conexion import Conexion;
from modelos.tiposcaso_modelo import ( TiposCaso)

class TiposCasoDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;


    # ----------------------------------------------------------
    # TIPOS CASO - SELECT todas
    # ----------------------------------------------------------
    def SelectTiposCaso(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_tiposCaso()}");

        listaTiposCaso: list = [];
        for fila in cursor:
            tipocaso = TiposCaso();
            tipocaso.idTipoCaso  = fila[0];
            tipocaso.nomTipo     = fila[1];
            tipocaso.descripcion = fila[2];
            tipocaso.tiempoMeta  = fila[3];
            tipocaso.activo      = fila[4];
            listaTiposCaso.append(tipocaso);

        cursor.close();
        con.close();
        return listaTiposCaso;

    # ----------------------------------------------------------
    # TIPOS CASO - SELECT por ID
    # ----------------------------------------------------------
    def SelectTiposCasoId(self, idTipoCaso: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_tipoCaso_id(?)}", idTipoCaso);

        tipocaso = None;
        for fila in cursor:
            tipocaso = TiposCaso();
            tipocaso.idTipoCaso  = fila[0];
            tipocaso.nomTipo     = fila[1];
            tipocaso.descripcion = fila[2];
            tipocaso.tiempoMeta  = fila[3];
            tipocaso.activo      = fila[4];

        cursor.close();
        con.close();
        return tipocaso;
    # ----------------------------------------------------------
    # TIPOS CASO - INSERT
    # ----------------------------------------------------------
    def InsertTipoCaso(self, tipocaso: TiposCaso) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_tipoCaso(?, ?, ?, ?)}",
            tipocaso.nomTipo,
            tipocaso.descripcion,
            tipocaso.tiempoMeta,
            tipocaso.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # TIPOS CASO - UPDATE
    # ----------------------------------------------------------
    def UpdateTipoCaso(self, tipocaso: TiposCaso) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_tipoCaso(?, ?, ?, ?, ?)}",
            tipocaso.idTipoCaso,
            tipocaso.nomTipo,
            tipocaso.descripcion,
            tipocaso.tiempoMeta,
            tipocaso.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # TIPOS CASO - DELETE
    # ----------------------------------------------------------
    def DeleteTipoCaso(self, idTipoCaso: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_tipoCaso(?)}", idTipoCaso);
        con.commit();
        cursor.close();
        con.close();
