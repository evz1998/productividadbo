import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.areas_dao import AreasDAO
from modelos.areas_modelo import Areas

# ============================================================
# BLUEPRINT - AREAS
# ============================================================

areas_bp = flask.Blueprint("areas",__name__)

con = Conexion()
areasDAO = AreasDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# AREAS - GET todas
# ============================================================

@areas_bp.route("/main/SelectAreas", methods=["GET"])
def SelectAreas() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaArea = areasDAO.SelectAreas()
        areaJ = {}
        for area in listaArea:
            areaJ[str(area.idArea)] = {

                "idArea"        : area.idArea,
                "nomArea"       : area.nomArea,
                "descripcion"   : area.descripcion,
                "activa"        : area.activa
            }
        
        respuesta["AreaJson"] = areaJ
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
# AREAS - GET por ID
# ============================================================
    
@areas_bp.route("/main/SelectAreaID/<int:idArea>", methods=["GET"])
def SelectAreaID(idArea: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        area = areasDAO.SelectAreaId(idArea)
        
        if area: 
            respuesta["Entidad"] = {
                "idArea"        : area.idArea,
                "nomArea"       : area.nomArea,
                "descripcion"   : area.descripcion,
                "activa"        : area.activa
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
# AREAS - POST (INSERT)
# ============================================================

@areas_bp.route("/main/InsertArea", methods=["POST"])
def InsertArea() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevaarea               = Areas()
        nuevaarea.nomArea       = datos ["nomArea"]
        nuevaarea.descripcion   = datos ["descripcion"]
        nuevaarea.activa        = datos ["activa"]

        areasDAO.InsertArea(nuevaarea)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# AREAS - PUT (UPDATE)
# ============================================================
    
@areas_bp.route("/main/UpdateArea", methods=["PUT"])
def UpdateArea() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizararea               = Areas()
        actualizararea.idArea        = datos ["idArea"]
        actualizararea.nomArea       = datos ["nomArea"]
        actualizararea.descripcion   = datos ["descripcion"]
        actualizararea.activa        = datos ["activa"]

        areasDAO.UpdateArea(actualizararea)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# AREAS - DELETE 
# ============================================================

@areas_bp.route("/main/DeleteArea/<int:idArea>", methods=["DELETE"])
def DeleteArea(idArea: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        areasDAO.DeleteArea(idArea)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)