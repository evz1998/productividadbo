from conexion.conexion import Conexion;
from modelos.prioridades_modelo import (Prioridades)

class PrioridadesDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

 
    # ----------------------------------------------------------
    # PRIORIDADES - SELECT todas
    # ----------------------------------------------------------
    def SelectPrioridades(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_prioridades()}");

        listaPrioridades: list = [];
        for fila in cursor:
            prioridad = Prioridades();
            prioridad.idPrioridad  = fila[0];
            prioridad.nomPrioridad = fila[1];
            prioridad.nivel        = fila[2];
            prioridad.activa       = fila[3];
            listaPrioridades.append(prioridad);

        cursor.close();
        con.close();
        return listaPrioridades;

    # ----------------------------------------------------------
    # PRIORIDADES - SELECT por ID
    # ----------------------------------------------------------
    def SelectPrioridadId(self, idPrioridad: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_prioridad_id(?)}", idPrioridad);

        prioridad = None;
        for fila in cursor:
            prioridad = Prioridades();
            prioridad.idPrioridad  = fila[0];
            prioridad.nomPrioridad = fila[1];
            prioridad.nivel        = fila[2];
            prioridad.activa       = fila[3];

        cursor.close();
        con.close();
        return prioridad;

    # ----------------------------------------------------------
    # PRIORIDADES - INSERT
    # ----------------------------------------------------------
    def InsertPrioridad(self, prioridad: Prioridades) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_prioridad(?, ?, ?)}",
            prioridad.nomPrioridad,
            prioridad.nivel,
            prioridad.activa
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # PRIORIDADES - UPDATE
    # ----------------------------------------------------------
    def UpdatePrioridad(self, prioridad: Prioridades) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_prioridad(?, ?, ?, ?)}",
            prioridad.idPrioridad,
            prioridad.nomPrioridad,
            prioridad.nivel,
            prioridad.activa
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # PRIORIDADES - DELETE
    # ----------------------------------------------------------
    def DeletePrioridad(self, idPrioridad: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_prioridad(?)}", idPrioridad);
        con.commit();
        cursor.close();
        con.close();