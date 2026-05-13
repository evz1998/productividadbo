import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.evaluaciones_dao import EvaluacionesDAO
from modelos.evaluaciones_modelo import Evaluaciones

# ============================================================
# BLUEPRINT - EVALUACIONES
# ============================================================

evaluaciones_bp = flask.Blueprint("evaluaciones",__name__)

con = Conexion()
evaluacionesDAO = EvaluacionesDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# EVALUACIONES - GET todas
# ============================================================

@evaluaciones_bp.route("/main/SelectEvaluacionesCaso", methods=["GET"])
def SelectEvaluaciones() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaEvaluaciones = evaluacionesDAO.SelectEvaluaciones()
        evaluacionJ = {}
        for evaluacion in listaEvaluaciones:
            evaluacionJ[str(evaluacion.idEvaluacion)] = {


           "idEvaluacion"         :evaluacion.idEvaluacion,
           "idAsesor"             :evaluacion.idAsesor,
           "periodo"              :evaluacion.periodo,
           "calidad"              :evaluacion.calidad,
           "puntualidad"          :evaluacion.puntualidad,
           "casosGestionados"     :evaluacion.casosGestionados,
           "nota"                 :evaluacion.nota,
           "fechaEvaluacion"      :evaluacion.fechaEvaluacion

            }
        
        respuesta["EvaluacionJson"] = evaluacionJ
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
# EVALUACION - GET por ID
# ============================================================
    
@evaluaciones_bp.route("/main/SelectEvaluacionID/<int:idEvaluacion>", methods=["GET"])
def SelectEvaluacionID(idEvaluacion: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        evaluacion = evaluacionesDAO.SelectEvaluacionId(idEvaluacion)
        
        if evaluacion: 
            respuesta["Entidad"] = {
           
           "idEvaluacion"         :evaluacion.idEvaluacion,
           "idAsesor"             :evaluacion.idAsesor,
           "periodo"              :evaluacion.periodo,
           "calidad"              :evaluacion.calidad,
           "puntualidad"          :evaluacion.puntualidad,
           "casosGestionados"     :evaluacion.casosGestionados,
           "nota"                 :evaluacion.nota,
           "fechaEvaluacion"      :evaluacion.fechaEvaluacion

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
# EVALUACION - POST (INSERT)
# ============================================================

@evaluaciones_bp.route("/main/InsertEvaluacion", methods=["POST"])
def InsertEvaluacion() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevaevaluacion           = Evaluaciones()  

        nuevaevaluacion.idAsesor            = datos ["idAsesor"]
        nuevaevaluacion.periodo             = datos ["periodo"]
        nuevaevaluacion.calidad             = datos ["calidad"]
        nuevaevaluacion.puntualidad         = datos ["puntualidad"]
        nuevaevaluacion.casosGestionados    = datos ["casosGestionados"]
        nuevaevaluacion.nota                = datos ["nota"]
        nuevaevaluacion.fechaEvaluacion     = datos ["fechaEvaluacion"]

        evaluacionesDAO.InsertEvaluacion(nuevaevaluacion)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# EVALUACION - PUT (UPDATE)
# ============================================================
    
@evaluaciones_bp.route("/main/UpdateEvaluacion", methods=["PUT"])
def UpdateEvaluacion() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarevaluacion              = Evaluaciones()

        actualizarevaluacion.idEvaluacion           = datos ["idEvaluacion"]
        actualizarevaluacion.idAsesor               = datos ["idAsesor"]
        actualizarevaluacion.periodo                = datos ["periodo"]
        actualizarevaluacion.calidad                = datos ["calidad"]
        actualizarevaluacion.puntualidad            = datos ["puntualidad"]
        actualizarevaluacion.casosGestionados       = datos ["casosGestionados"]
        actualizarevaluacion.nota                   = datos ["nota"]
        actualizarevaluacion.fechaEvaluacion        = datos ["fechaEvaluacion"]

        evaluacionesDAO.UpdateEvaluacion(actualizarevaluacion)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# EVALUACION - DELETE 
# ============================================================

@evaluaciones_bp.route("/main/DeleteEvaluacion/<int:idEvaluacion>", methods=["DELETE"])
def DeleteEvaluacion(idEvaluacion: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        evaluacionesDAO.DeleteEvaluacion(idEvaluacion)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)