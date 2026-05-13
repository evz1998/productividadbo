from conexion.conexion import Conexion;
from modelos.turnos_modelo import (Turnos)

class TurnosDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

    # ----------------------------------------------------------
    #   TURNOS - SELECT todas
    # ----------------------------------------------------------
    def SelectTurnos(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_turnos()}");

        listaTurnos: list = [];
        for fila in cursor:
            turno = Turnos();
            turno.idTurno      = fila[0];
            turno.nomturno     = fila[1];
            turno.horaInicio   = fila[2];
            turno.horaFin      = fila[3];
            turno.activo       = fila[4];
            listaTurnos.append(turno);

        cursor.close();
        con.close();
        return listaTurnos;

    # ----------------------------------------------------------
    # TURNOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectTurnoId(self, idTurno: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_turno_id(?)}", idTurno);

        turno = None;
        for fila in cursor:
            turno = Turnos();
            turno.idTurno      = fila[0];
            turno.nomturno     = fila[1];
            turno.horaInicio   = fila[2];
            turno.horaFin      = fila[3];
            turno.activo       = fila[4];
        cursor.close();
        con.close();
        return turno;

    # ----------------------------------------------------------
    # TURNOS - INSERT
    # ----------------------------------------------------------
    def InsertTurno(self, turno: Turnos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_turno(?, ?, ?, ?)}",
            turno.nomturno,
            turno.horaInicio,
            turno.horaFin,
            turno.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # TURNOS - UPDATE
    # ----------------------------------------------------------
    def UpdateTurno(self, turno: Turnos) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_turno(?, ?, ?, ?, ?)}",
            turno.idTurno,
            turno.nomturno,
            turno.horaInicio,
            turno.horaFin,
            turno.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # TURNOS - DELETE
    # ----------------------------------------------------------
    def DeleteTurno(self, idTurno: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_turno(?)}", idTurno);
        con.commit();
        cursor.close();
        con.close();