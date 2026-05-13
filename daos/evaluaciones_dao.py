from conexion.conexion import Conexion;
from modelos.evaluaciones_modelo import (Evaluaciones)

class EvaluacionesDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;  

    # ----------------------------------------------------------
    #   EVALUACIONES - SELECT todas
    # ----------------------------------------------------------
    def SelectEvaluaciones(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_evaluaciones()}");

        listaEvaluaciones: list = [];
        for fila in cursor:
            evaluacion = Evaluaciones();
            evaluacion.idEvaluacion      = fila[0];
            evaluacion.idAsesor          = fila[1];
            evaluacion.periodo           = fila[2];
            evaluacion.calidad           = fila[3];
            evaluacion.puntualidad       = fila[4];
            evaluacion.casosGestionados  = fila[5];
            evaluacion.nota              = fila[6];
            evaluacion.fechaEvaluacion   = fila[7];
            listaEvaluaciones.append(evaluacion);

        cursor.close();
        con.close();
        return listaEvaluaciones;

    # ----------------------------------------------------------
    # EVALUACIONES - SELECT por ID
    # ----------------------------------------------------------
    def SelectEvaluacionId(self, idEvaluacion: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_evaluacion_id(?)}", idEvaluacion);

        evaluacion = None;
        for fila in cursor:
            evaluacion = Evaluaciones();
            evaluacion.idEvaluacion      = fila[0];
            evaluacion.idAsesor          = fila[1];
            evaluacion.periodo           = fila[2];
            evaluacion.calidad           = fila[3];
            evaluacion.puntualidad       = fila[4];
            evaluacion.casosGestionados  = fila[5];
            evaluacion.nota              = fila[6];
            evaluacion.fechaEvaluacion   = fila[7];
        cursor.close();
        con.close();
        return evaluacion;

    # ----------------------------------------------------------
    # EVALUACIONES - INSERT
    # ----------------------------------------------------------
    def InsertEvaluacion(self, evaluacion: Evaluaciones) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_evaluacion(?, ?, ?, ?, ?, ?, ?)}",
            evaluacion.idAsesor,
            evaluacion.periodo,
            evaluacion.calidad,
            evaluacion.puntualidad,
            evaluacion.casosGestionados,
            evaluacion.nota,
            evaluacion.fechaEvaluacion
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # EVALUACIONES - UPDATE
    # ----------------------------------------------------------
    def UpdateEvaluacion(self, evaluacion: Evaluaciones) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_evaluacion(?, ?, ?, ?, ?, ?, ?, ?)}",
            evaluacion.idEvaluacion,
            evaluacion.idAsesor,
            evaluacion.periodo,
            evaluacion.calidad,
            evaluacion.puntualidad,
            evaluacion.casosGestionados,
            evaluacion.nota,
            evaluacion.fechaEvaluacion
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # EVALUACIONES - DELETE
    # ----------------------------------------------------------
    def DeleteEvaluacion(self, idEvaluacion: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_evaluacion(?)}", idEvaluacion);
        con.commit();
        cursor.close();
        con.close();