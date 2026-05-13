import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.prioridades_dao import PrioridadesDAO
from modelos.prioridades_modelo import Prioridades

# ============================================================
# BLUEPRINT - PRIORIDADES
# ============================================================

prioridad_bp = flask.Blueprint("prioridad",__name__)

con = Conexion()
prioridadDAO = PrioridadesDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# PRIORIDAD - GET todas
# ============================================================

@prioridad_bp.route("/main/SelectPrioridad", methods=["GET"])
def SelectPrioridad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaPrioridad = prioridadDAO.SelectPrioridades()
        prioridadJ = {}
        for prioridad in listaPrioridad:
            prioridadJ[str(prioridad.idPrioridad)] = {

            "idPrioridad"           :prioridad.idPrioridad,
            "nomPrioridad"          :prioridad.nomPrioridad, 
            "nivel"                 :prioridad.nivel,
            "activa"                :prioridad.activa

            }
        
        respuesta["PrioridadJson"] = prioridadJ
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
# PRIORIDAD - GET por ID
# ============================================================
    
@prioridad_bp.route("/main/SelectPrioridadID/<int:idPrioridad>", methods=["GET"])
def SelectPrioridadID(idPrioridad: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        prioridad = prioridadDAO.SelectPrioridadId(idPrioridad)
        
        if prioridad: 
            respuesta["Entidad"] = {
           
            "idPrioridad"           :prioridad.idPrioridad,
            "nomPrioridad"          :prioridad.nomPrioridad, 
            "nivel"                 :prioridad.nivel,
            "activa"                :prioridad.activa

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
# PRIORIDAD - POST (INSERT)
# ============================================================

@prioridad_bp.route("/main/InsertPrioridad", methods=["POST"])
def InsertPrioridad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevaprioridad           = Prioridades()  

        nuevaprioridad.nomPrioridad     = datos ["nomPrioridad"]
        nuevaprioridad.nivel            = datos ["nivel"]
        nuevaprioridad.activa           = datos ["activa"]
     

        prioridadDAO.InsertPrioridad(nuevaprioridad)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# PRIORIDAD - PUT (UPDATE)
# ============================================================
    
@prioridad_bp.route("/main/UpdatePrioridad", methods=["PUT"])
def UpdatePrioridad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarprioridad                  = Prioridades()

        actualizarprioridad.idPrioridad      = datos ["idPrioridad"]
        actualizarprioridad.nomPrioridad     = datos ["nomPrioridad"]
        actualizarprioridad.nivel            = datos ["nivel"]
        actualizarprioridad.activa           = datos ["activa"]

        prioridadDAO.UpdatePrioridad(actualizarprioridad)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# PRIORIDAD - DELETE 
# ============================================================

@prioridad_bp.route("/main/DeletePrioridad/<int:idPrioridad>", methods=["DELETE"])
def DeletePrioridad(idPrioridad: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        prioridadDAO.DeletePrioridad(idPrioridad)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)