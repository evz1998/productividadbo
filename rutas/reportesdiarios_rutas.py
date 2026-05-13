import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.reportesdiarios_dao import ReportesDiariosDAO
from modelos.reportediarios_modelo import ReportesDiarios

# ============================================================
# BLUEPRINT - REPORTES DIARIOS
# ============================================================

reportediario_bp = flask.Blueprint("reportediario",__name__)

con = Conexion()
reportediarioDAO = ReportesDiariosDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# REPORTE DIARIOS - GET todas
# ============================================================

@reportediario_bp.route("/main/SelectReportesDiarios", methods=["GET"])
def SelectReportesDiarios() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaReporteDiario = reportediarioDAO.SelectReportesDiarios()
        reportediarioJ = {}
        for reporte in listaReporteDiario:
            reportediarioJ[str(reporte.idReporte)] = {

            "idReporte"            :reporte.idReporte,
            "idAsesor"             :reporte.idAsesor,
            "fecha"                :reporte.fecha,
            "casosAbiertos"        :reporte.casosAbiertos,
            "casosCerrados"        :reporte.casosCerrados,
            "casosEnProceso"       :reporte.casosEnProceso,
            "tiempoPromedio"       :reporte.tiempoPromedio,
            "cumplioMeta"          :reporte.cumplioMeta   

            }
        
        respuesta["ReporteJson"] = reportediarioJ
        respuesta["Respuesta"] = "OK"
        return flask.Response(
            json.dumps(respuesta, default=convertir, indent=4, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# REPORTE DIARIO - GET por ID
# ============================================================
    
@reportediario_bp.route("/main/SelectReporteDiarioID/<int:idReporte>", methods=["GET"])
def SelectReporteDiarioID(idReporte: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        reporte = reportediarioDAO.SelectReporteDiarioId(idReporte)
        
        if reporte: 
            respuesta["Entidad"] = {
           
            "idReporte"            :reporte.idReporte,
            "idAsesor"             :reporte.idAsesor,
            "fecha"                :reporte.fecha,
            "casosAbiertos"        :reporte.casosAbiertos,
            "casosCerrados"        :reporte.casosCerrados,
            "casosEnProceso"       :reporte.casosEnProceso,
            "tiempoPromedio"       :reporte.tiempoPromedio,
            "cumplioMeta"          :reporte.cumplioMeta  

            }
            respuesta["Respuesta"] = "OK"
        else:
            respuesta["Respuesta"] = "NOT FOUND"
        return flask.Response(
           json.dumps(respuesta, default=convertir, indent=4, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# REPORTE DIARIO - POST (INSERT)
# ============================================================

@reportediario_bp.route("/main/InsertReporteDiario", methods=["POST"])
def InsertReporteDiario() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoreporte           = ReportesDiarios() 

        nuevoreporte.idAsesor             = datos ["idAsesor"]
        nuevoreporte.fecha                = datos ["fecha"]
        nuevoreporte.casosAbiertos        = datos ["casosAbiertos"]
        nuevoreporte.casosCerrados        = datos ["casosCerrados"]
        nuevoreporte.casosEnProceso       = datos ["casosEnProceso"]
        nuevoreporte.tiempoPromedio       = datos ["tiempoPromedio"]
        nuevoreporte.cumplioMeta          = datos ["cumplioMeta"]

        reportediarioDAO.InsertReporteDiario(nuevoreporte)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# REPORTE DIARIO - PUT (UPDATE)
# ============================================================
    
@reportediario_bp.route("/main/UpdateReporteDiario", methods=["PUT"])
def UpdateReporteDiario() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarreporte                  = ReportesDiarios()

  
        actualizarreporte.idReporte           = datos ["idReporte"]
        actualizarreporte.idAsesor            = datos ["idAsesor"]
        actualizarreporte.fecha               = datos ["fecha"]
        actualizarreporte.casosAbiertos       = datos ["casosAbiertos"]
        actualizarreporte.casosCerrados       = datos ["casosCerrados"]
        actualizarreporte.casosEnProceso      = datos ["casosEnProceso"]
        actualizarreporte.tiempoPromedio      = datos ["tiempoPromedio"]
        actualizarreporte.cumplioMeta         = datos ["cumplioMeta"]

        reportediarioDAO.UpdateReporteDiario(actualizarreporte)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# REPORTE DIARIO - DELETE 
# ============================================================

@reportediario_bp.route("/main/DeleteReporteDiario/<int:idReporte>", methods=["DELETE"])
def DeleteReporteDiario(idReporte: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        reportediarioDAO.DeleteReporteDiario(idReporte)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)