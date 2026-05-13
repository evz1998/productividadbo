from conexion.conexion import Conexion;
from modelos.metasproductividad_modelo import (MetasProductividad)

class MetasProductividadDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;  

    # ----------------------------------------------------------
    #   METAS PRODUCTIVIDAD - SELECT todas
    # ----------------------------------------------------------
    def SelectMetasProductividad(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_metas()}");

        listaMetas: list = [];
        for fila in cursor:
            meta = MetasProductividad();
            meta.idMeta          = fila[0];
            meta.idArea          = fila[1];
            meta.idTipoCaso      = fila[2];
            meta.casosMetaDia    = fila[3];
            meta.vigenciaDesde   = fila[4];
            meta.vigenciaHasta   = fila[5];
            meta.activa          = fila[6];
            listaMetas.append(meta);

        cursor.close();
        con.close();
        return listaMetas;

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - SELECT por ID
    # ----------------------------------------------------------
    def SelectMetaProductividadId(self, idMeta: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_meta_id(?)}", idMeta);

        meta = None;
        for fila in cursor:
            meta = MetasProductividad();
            meta.idMeta          = fila[0];
            meta.idArea          = fila[1];
            meta.idTipoCaso      = fila[2];
            meta.casosMetaDia    = fila[3];
            meta.vigenciaDesde   = fila[4];
            meta.vigenciaHasta   = fila[5];
            meta.activa          = fila[6];
        cursor.close();
        con.close();
        return meta;

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - INSERT
    # ----------------------------------------------------------
    def InsertMeta(self, meta: MetasProductividad) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_meta(?, ?, ?, ?, ?, ?)}",
            meta.idArea,
            meta.idTipoCaso,
            meta.casosMetaDia,
            meta.vigenciaDesde,
            meta.vigenciaHasta,
            meta.activa
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - UPDATE
    # ----------------------------------------------------------
    def UpdateMetaProductividad(self, meta: MetasProductividad) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_meta(?, ?, ?, ?, ?, ?, ?)}",
            meta.idMeta,
            meta.idArea,
            meta.idTipoCaso,
            meta.casosMetaDia,
            meta.vigenciaDesde,
            meta.vigenciaHasta,
            meta.activa
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - DELETE
    # ----------------------------------------------------------
    def DeleteMetaProductividad(self, idMeta: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_meta(?)}", idMeta);
        con.commit();
        cursor.close();
        con.close();