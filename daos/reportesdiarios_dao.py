from conexion.conexion import Conexion;
from modelos.reportediarios_modelo import (ReportesDiarios)

class ReportesDiariosDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;  

    # ----------------------------------------------------------
    #   REPORTES DIARIOS - SELECT todas
    # ----------------------------------------------------------
    def SelectReportesDiarios(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_reportes()}");

        listaReportes: list = [];
        for fila in cursor:
            reporte = ReportesDiarios();
            reporte.idReporte      = fila[0];
            reporte.idAsesor       = fila[1];
            reporte.fecha          = fila[2];
            reporte.casosAbiertos  = fila[3];
            reporte.casosCerrados  = fila[4];
            reporte.casosEnProceso = fila[5];
            reporte.tiempoPromedio = fila[6];
            reporte.cumplioMeta    = fila[7];
            listaReportes.append(reporte);

        cursor.close();
        con.close();
        return listaReportes;

    # ----------------------------------------------------------
    # REPORTES DIARIOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectReporteDiarioId(self, idReporte: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_reporte_id(?)}", idReporte);

        reporte = None;
        for fila in cursor:
            reporte = ReportesDiarios();
            reporte.idReporte      = fila[0];
            reporte.idAsesor       = fila[1];
            reporte.fecha          = fila[2];
            reporte.casosAbiertos  = fila[3];
            reporte.casosCerrados  = fila[4];
            reporte.casosEnProceso = fila[5];
            reporte.tiempoPromedio = fila[6];
            reporte.cumplioMeta    = fila[7];
        cursor.close();
        con.close();
        return reporte;

    # ----------------------------------------------------------
    # REPORTES DIARIOS - INSERT
    # ----------------------------------------------------------
    def InsertReporteDiario(self, reporte: ReportesDiarios) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_reporte(?, ?, ?, ?, ?, ?, ?)}",
            reporte.idAsesor,
            reporte.fecha,
            reporte.casosAbiertos,
            reporte.casosCerrados,
            reporte.casosEnProceso,
            reporte.tiempoPromedio,
            reporte.cumplioMeta
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # REPORTE DIARIOS - UPDATE
    # ----------------------------------------------------------
    def UpdateReporteDiario(self, reporte: ReportesDiarios) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_reporte(?, ?, ?, ?, ?, ?, ?, ?)}",
            reporte.idReporte,
            reporte.idAsesor,
            reporte.fecha,
            reporte.casosAbiertos,
            reporte.casosCerrados,
            reporte.casosEnProceso,
            reporte.tiempoPromedio,
            reporte.cumplioMeta
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # REPORTE DIARIOS - DELETE
    # ----------------------------------------------------------
    def DeleteReporteDiario(self, idReporte: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_reporte(?)}", idReporte);
        con.commit();
        cursor.close();
        con.close();
