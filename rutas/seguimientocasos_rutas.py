import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.seguimientocasos_dao import SeguimientoCasosDAO
from modelos.seguimientocasos_modelo import seguimientoCasos

# ============================================================
# BLUEPRINT - SEGUIMIENTO CASOS
# ============================================================

seguimientocasos_bp = flask.Blueprint("seguimientocasos",__name__)

con = Conexion()
seguimientocasosDAO = SeguimientoCasosDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# SEGUIMIENTO CASOS - GET todas
# ============================================================

@seguimientocasos_bp.route("/main/SelectSeguimientoCasos", methods=["GET"])
def SelectSeguimientoCasos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaSeguimiento = seguimientocasosDAO.SelectSeguimientos()
        seguimientoJ = {}
        for seguimiento in listaSeguimiento:
            seguimientoJ[str(seguimiento.idSeguimiento)] = {

            "idSeguimiento"        :seguimiento.idSeguimiento,
            "idCaso"               :seguimiento.idCaso,
            "idAsesor"             :seguimiento.idAsesor,
            "idEstado"             :seguimiento.idEstado,
            "nota"                 :seguimiento.nota,
            "fecharegistro"        :seguimiento.fecharegistro

            }
        
        respuesta["SeguimientoJson"] = seguimientoJ
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
# SEGUIMIENTO CASOS - GET por ID
# ============================================================
    
@seguimientocasos_bp.route("/main/SelectSeguimientoCasoID/<int:idSeguimiento>", methods=["GET"])
def SelectSeguimientoCasoID(idSeguimiento: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        seguimiento = seguimientocasosDAO.SelectSeguimientoId(idSeguimiento)
        
        if seguimiento: 
            respuesta["Entidad"] = {
           
            "idSeguimiento"        :seguimiento.idSeguimiento,
            "idCaso"               :seguimiento.idCaso,
            "idAsesor"             :seguimiento.idAsesor,
            "idEstado"             :seguimiento.idEstado,
            "nota"                 :seguimiento.nota,
            "fecharegistro"        :seguimiento.fecharegistro

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
# SEGUIMIENTO CASOS - POST (INSERT)
# ============================================================

@seguimientocasos_bp.route("/main/InsertSeguimientoCaso", methods=["POST"])
def InsertSeguimientoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoseguimiento                  = seguimientoCasos() 

        nuevoseguimiento.idCaso                  = datos ["idCaso"]
        nuevoseguimiento.idAsesor                = datos ["idAsesor"]
        nuevoseguimiento.idEstado                = datos ["idEstado"]
        nuevoseguimiento.nota                    = datos ["nota"]
        nuevoseguimiento.fecharegistro           = datos ["fecharegistro"]
        

        seguimientocasosDAO.InsertSeguimiento(nuevoseguimiento)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# SEGUIMIENTO CASOS - PUT (UPDATE)
# ============================================================
    
@seguimientocasos_bp.route("/main/UpdateSeguimientoCaso", methods=["PUT"])
def UpdateSeguimientoCaso() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarseguimiento                  = seguimientoCasos()

        actualizarseguimiento.idSeguimiento           = datos ["idSeguimiento"]
        actualizarseguimiento.idCaso                  = datos ["idCaso"]
        actualizarseguimiento.idAsesor                = datos ["idAsesor"]
        actualizarseguimiento.idEstado                = datos ["idEstado"]
        actualizarseguimiento.nota                    = datos ["nota"]
        actualizarseguimiento.fecharegistro           = datos ["fecharegistro"]

        seguimientocasosDAO.UpdateSeguimiento(actualizarseguimiento)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# SEGUIMIENTO CASO - DELETE 
# ============================================================

@seguimientocasos_bp.route("/main/DeleteSeguimientoCaso/<int:idSeguimiento>", methods=["DELETE"])
def DeleteSeguimientoCaso(idSeguimiento: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        seguimientocasosDAO.DeleteSeguimiento(idSeguimiento)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)