from conexion.conexion import Conexion;
from conexion.encriptacion import encriptar, desencriptar;
from modelos.casos_modelo import (Casos)

class CasosDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;


    # ----------------------------------------------------------
    #   CASOS - SELECT todas
    # ----------------------------------------------------------
    def SelectCasos(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_casos()}");

        listaCasos: list = [];
        for fila in cursor:
            caso = Casos();
            caso.idCaso          = fila[0];
            caso.idCliente       = fila[1];
            caso.idTipoCaso      = fila[2];
            caso.idPrioridad     = fila[3];
            caso.idCanal         = fila[4];
            caso.idEstado        = fila[5];
            caso.idAsesor        = fila[6];
            caso.descripcion     = desencriptar(fila[7]);
            caso.fechaApertura   = fila[8];
            caso.fechaCierre     = fila[9];
            listaCasos.append(caso);

        cursor.close();
        con.close();
        return listaCasos;

    # ----------------------------------------------------------
    # CASOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectCasosId(self, idCaso: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_caso_id(?)}", idCaso);

        caso = None;
        for fila in cursor:
            caso = Casos();
            caso.idCaso          = fila[0];
            caso.idCliente       = fila[1];
            caso.idTipoCaso      = fila[2];
            caso.idPrioridad     = fila[3];
            caso.idCanal         = fila[4];
            caso.idEstado        = fila[5];
            caso.idAsesor        = fila[6];
            caso.descripcion     = desencriptar(fila[7]);
            caso.fechaApertura   = fila[8];
            caso.fechaCierre     = fila[9];

        cursor.close();
        con.close();
        return caso;

    # ----------------------------------------------------------
    # CASOS - INSERT
    # ----------------------------------------------------------
    def InsertCasos(self, caso: Casos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_caso(?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            caso.idCliente,
            caso.idTipoCaso,
            caso.idPrioridad,
            caso.idCanal,
            caso.idEstado,
            caso.idAsesor,
            encriptar(caso.descripcion),
            caso.fechaApertura,
            caso.fechaCierre
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CASOS - UPDATE
    # ----------------------------------------------------------
    def UpdateCasos(self, caso: Casos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_caso(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            caso.idCaso,
            caso.idCliente,
            caso.idTipoCaso,
            caso.idPrioridad,
            caso.idCanal,
            caso.idEstado,
            caso.idAsesor,
            encriptar(caso.descripcion),
            caso.fechaApertura,
            caso.fechaCierre
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # CASOS - DELETE
    # ----------------------------------------------------------
    def DeleteCasos(self, idCaso: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_caso(?)}", idCaso);
        con.commit();
        cursor.close();
        con.close();