import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.tiposcaso_dao import TiposCasoDAO
from modelos.tiposcaso_modelo import TiposCaso

# ============================================================
# BLUEPRINT - TIPOS CASO
# ============================================================

tiposcasos_bp = flask.Blueprint("tipocasos",__name__)

con = Conexion()
tipocasosDAO = TiposCasoDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# TIPOS CASOS - GET todas
# ============================================================

@tiposcasos_bp.route("/main/SelectTipoCasos", methods=["GET"])
def SelectTipoCasos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaTiposCaso = tipocasosDAO.SelectTiposCaso()
        tipocasoJ = {}
        for tipocaso in listaTiposCaso:
            tipocasoJ[str(tipocaso.idTipoCaso)] = {

            "idTipoCaso"           :tipocaso.idTipoCaso,
            "nomTipo"              :tipocaso.nomTipo,
            "descripcion"          :tipocaso.descripcion,
            "tiempoMeta"           :tipocaso.tiempoMeta,
            "activo"               :tipocaso.activo,

            }
        
        respuesta["TipoCasoJson"] = tipocasoJ
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
# TIPO CASOS - GET por ID
# ============================================================
    
@tiposcasos_bp.route("/main/SelectTipoCasoID/<int:idTipoCaso>", methods=["GET"])
def SelectTipoCasoID(idTipoCaso: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        tipocaso = tipocasosDAO.SelectTiposCasoId(idTipoCaso)
        
        if tipocaso: 
            respuesta["Entidad"] = {
           
            "idTipoCaso"           :tipocaso.idTipoCaso,
            "nomTipo"              :tipocaso.nomTipo,
            "descripcion"          :tipocaso.descripcion,
            "tiempoMeta"           :tipocaso.tiempoMeta,
            "activo"               :tipocaso.activo,

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
# TIPO CASOS - POST (INSERT)
# ============================================================

@tiposcasos_bp.route("/main/InsertTipoCaso", methods=["POST"])
def InsertTipoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevotipocaso                 = TiposCaso() 

        nuevotipocaso.nomTipo                  = datos ["nomTipo"]
        nuevotipocaso.descripcion              = datos ["descripcion"]
        nuevotipocaso.tiempoMeta               = datos ["tiempoMeta"]
        nuevotipocaso.activo                   = datos ["activo"]  

        tipocasosDAO.InsertTipoCaso(nuevotipocaso)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# TIPO CASOS - PUT (UPDATE)
# ============================================================
    
@tiposcasos_bp.route("/main/UpdateTipoCaso", methods=["PUT"])
def UpdateTipoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizartipocaso                  = TiposCaso()

        actualizartipocaso.idTipoCaso               = datos ["idTipoCaso"]
        actualizartipocaso.nomTipo                  = datos ["nomTipo"]
        actualizartipocaso.descripcion              = datos ["descripcion"]
        actualizartipocaso.tiempoMeta               = datos ["tiempoMeta"]
        actualizartipocaso.activo                   = datos ["activo"]  

        tipocasosDAO.UpdateTipoCaso(actualizartipocaso)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# TIPO CASO - DELETE 
# ============================================================

@tiposcasos_bp.route("/main/DeleteTipoCaso/<int:idTipoCaso>", methods=["DELETE"])
def DeleteTipoCaso(idTipoCaso: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        tipocasosDAO.DeleteTipoCaso(idTipoCaso)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)