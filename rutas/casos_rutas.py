import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.casos_dao import CasosDAO
from modelos.casos_modelo import Casos

# ============================================================
# BLUEPRINT - CASOS
# ============================================================

casos_bp = flask.Blueprint("casos",__name__)

con = Conexion()
casosDAO = CasosDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# CASOS - GET todas
# ============================================================

@casos_bp.route("/main/SelectCasos", methods=["GET"])
def SelectCasos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaCaso = casosDAO.SelectCasos()
        casoJ = {}
        for caso in listaCaso:
            casoJ[str(caso.idCaso)] = {

            "idCaso"             :caso.idCaso,
            "idCliente"          :caso.idCliente,
            "idTipoCaso"         :caso.idTipoCaso,
            "idPrioridad"        :caso.idPrioridad,
            "idCanal"            :caso.idCanal,
            "idEstado"           :caso.idEstado,
            "idAsesor"           :caso.idAsesor,
            "descripcion"        :caso.descripcion,
            "fechaApertura"      :caso.fechaApertura,
            "fechaCierre"        :caso.fechaCierre

            }
        
        respuesta["CasoJson"] = casoJ
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
# CASOS - GET por ID
# ============================================================
    
@casos_bp.route("/main/SelectCasosID/<int:idCaso>", methods=["GET"])
def SelectCasosID(idCaso: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        caso = casosDAO.SelectCasosId(idCaso)
        
        if caso: 
            respuesta["Entidad"] = {
              
            "idCaso"             :caso.idCaso,
            "idCliente"          :caso.idCliente,
            "idTipoCaso"         :caso.idTipoCaso,
            "idPrioridad"        :caso.idPrioridad,
            "idCanal"            :caso.idCanal,
            "idEstado"           :caso.idEstado,
            "idAsesor"           :caso.idAsesor,
            "descripcion"        :caso.descripcion,
            "fechaApertura"      :caso.fechaApertura,
            "fechaCierre"        :caso.fechaCierre

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
# CASOS - POST (INSERT)
# ============================================================

@casos_bp.route("/main/InsertCasos", methods=["POST"])
def InsertCasos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevocaso               = Casos()

        nuevocaso.idCliente       = datos ["idCliente"]
        nuevocaso.idTipoCaso      = datos ["idTipoCaso"]
        nuevocaso.idPrioridad     = datos ["idPrioridad"]
        nuevocaso.idCanal         = datos ["idCanal"]
        nuevocaso.idEstado        = datos ["idEstado"]
        nuevocaso.idAsesor        = datos ["idAsesor"]
        nuevocaso.descripcion     = datos ["descripcion"]
        nuevocaso.fechaApertura   = datos ["fechaApertura"]
        nuevocaso.fechaCierre     = datos ["fechaCierre"]

        casosDAO.InsertCasos(nuevocaso)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CASOS - PUT (UPDATE)
# ============================================================
    
@casos_bp.route("/main/UpdateCasos", methods=["PUT"])
def UpdateCasos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarcaso               = Casos()

        actualizarcaso.idCaso          = datos ["idCaso"]
        actualizarcaso.idCliente       = datos ["idCliente"]
        actualizarcaso.idTipoCaso      = datos ["idTipoCaso"]
        actualizarcaso.idPrioridad     = datos ["idPrioridad"]
        actualizarcaso.idCanal         = datos ["idCanal"]
        actualizarcaso.idEstado        = datos ["idEstado"]
        actualizarcaso.idAsesor        = datos ["idAsesor"]
        actualizarcaso.descripcion     = datos ["descripcion"]
        actualizarcaso.fechaApertura   = datos ["fechaApertura"]
        actualizarcaso.fechaCierre     = datos ["fechaCierre"]
        

        casosDAO.UpdateCasos(actualizarcaso)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CASOS - DELETE 
# ============================================================

@casos_bp.route("/main/DeleteCasos/<int:idCaso>", methods=["DELETE"])
def DeleteCasos(idCaso: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        casosDAO.DeleteCasos(idCaso)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)