from conexion.conexion import Conexion;
from modelos.asistencia_modelo import (Asistencia)

class AsistenciaDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;

    # ----------------------------------------------------------
    #   ASISTENCIAS - SELECT todas
    # ----------------------------------------------------------
    def SelectAsistencias(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_asistencias()}");

        listaAsistencias: list = [];
        for fila in cursor:
            asistencia = Asistencia();
            asistencia.idAsistencia      = fila[0];
            asistencia.idAsesor          = fila[1];
            asistencia.idTurno           = fila[2];
            asistencia.fecha             = fila[3];
            asistencia.horaEntrada       = fila[4];
            asistencia.horaSalida        = fila[5];
            asistencia.minutosTrabajados = fila[6];
            listaAsistencias.append(asistencia);

        cursor.close();
        con.close();
        return listaAsistencias;

    # ----------------------------------------------------------
    # ASISTENCIA - SELECT por ID
    # ----------------------------------------------------------
    def SelectAsistenciaId(self, idAsistencia: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_asistencia_id(?)}", idAsistencia);

        asistencia = None;
        for fila in cursor:
            asistencia = Asistencia();
            asistencia.idAsistencia      = fila[0];
            asistencia.idAsesor          = fila[1];
            asistencia.idTurno           = fila[2];
            asistencia.fecha             = fila[3];
            asistencia.horaEntrada       = fila[4];
            asistencia.horaSalida        = fila[5];
            asistencia.minutosTrabajados = fila[6];
        cursor.close();
        con.close();
        return asistencia;

    # ----------------------------------------------------------
    # ASISTENCIA - INSERT
    # ----------------------------------------------------------
    def InsertAsistencia(self, asistencia: Asistencia) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_asistencia(?, ?, ?, ?, ?, ?)}",
            asistencia.idAsesor,
            asistencia.idTurno,
            asistencia.fecha,
            asistencia.horaEntrada,
            asistencia.horaSalida,
            asistencia.minutosTrabajados
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # ASISTENCIA - UPDATE
    # ----------------------------------------------------------
    def UpdateAsistencia(self, asistencia: Asistencia) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_asistencia(?, ?, ?, ?, ?, ?, ?)}",
            asistencia.idAsistencia,
            asistencia.idAsesor,
            asistencia.idTurno,
            asistencia.fecha,
            asistencia.horaEntrada,
            asistencia.horaSalida,
            asistencia.minutosTrabajados
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # ASISTENCIA - DELETE
    # ----------------------------------------------------------
    def DeleteAsistencia(self, idAsistencia: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_asistencia(?)}", idAsistencia);
        con.commit();
        cursor.close();
        con.close();