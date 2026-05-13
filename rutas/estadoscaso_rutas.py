import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.estadoscaso_dao import EstadosCasoDAO
from modelos.estadoscaso_modelo import estadosCaso

# ============================================================
# BLUEPRINT - ESTADOS CASO
# ============================================================

estadocaso_bp = flask.Blueprint("estadocaso",__name__)

con = Conexion()
estadocasoDAO = EstadosCasoDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# ESTADOS CASO - GET todas
# ============================================================

@estadocaso_bp.route("/main/SelectEstadosCaso", methods=["GET"])
def SelectEstadosCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaEstadoCaso = estadocasoDAO.SelectEstadosCaso()
        estadocasoJ = {}
        for estadocaso in listaEstadoCaso:
            estadocasoJ[str(estadocaso.idEstadoCaso)] = {

            "idEstado"             :estadocaso.idEstado,
            "nomEstado"            :estadocaso.nomEstado,
            "descripcion"          :estadocaso.descripcion,
            "esfinal"              :estadocaso.esfinal,
            "activo"               :estadocaso.activo

            }
        
        respuesta["EstadoCasoJson"] = estadocasoJ
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
# ESTADO CASOS - GET por ID
# ============================================================
    
@estadocaso_bp.route("/main/SelectEstadoCasoID/<int:idEstado>", methods=["GET"])
def SelectEstadoCasoID(idEstado: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        estadocaso = estadocasoDAO.SelectEstadoCasoId(idEstado)
        
        if estadocaso: 
            respuesta["Entidad"] = {

            "idEstado"             :estadocaso.idEstado,
            "nomEstado"            :estadocaso.nomEstado,
            "descripcion"          :estadocaso.descripcion,
            "esfinal"              :estadocaso.esfinal,
            "activo"               :estadocaso.activo  

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
# ESTADO CASO - POST (INSERT)
# ============================================================

@estadocaso_bp.route("/main/InsertEstadoCaso", methods=["POST"])
def InsertEstadoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoestado               = estadosCaso()  

        nuevoestado.nomEstado       = datos ["nomEstado"]
        nuevoestado.descripcion     = datos ["descripcion"]
        nuevoestado.esfinal         = datos ["esfinal"]
        nuevoestado.activo          = datos ["activo"]

        estadocasoDAO.InsertEstadoCaso(nuevoestado)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# ESTADO CASO - PUT (UPDATE)
# ============================================================
    
@estadocaso_bp.route("/main/UpdateEstadoCaso", methods=["PUT"])
def UpdateEstadoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarestado              = estadosCaso()

        actualizarestado.idEstado       = datos ["idEstado"]
        actualizarestado.nomEstado      = datos ["nomEstado"]
        actualizarestado.descripcion    = datos ["descripcion"]
        actualizarestado.esfinal        = datos ["esfinal"]
        actualizarestado.activo         = datos ["activo"]

        estadocasoDAO.UpdateEstadoCaso(actualizarestado)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# ESTADO CASO - DELETE 
# ============================================================

@estadocaso_bp.route("/main/DeleteEstadoCaso/<int:idEstado>", methods=["DELETE"])
def DeleteEstadoCaso(idEstado: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        estadocasoDAO.DeleteEstadoCaso(idEstado)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)