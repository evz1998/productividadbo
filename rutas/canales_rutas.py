import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.canales_dao import CanalesDAO
from modelos.canales_modelo import Canales

# ============================================================
# BLUEPRINT - CANALES
# ============================================================

canal_bp = flask.Blueprint("canal",__name__)

con = Conexion()
canalDAO = CanalesDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# CANALES - GET todas
# ============================================================

@canal_bp.route("/main/SelectCanales", methods=["GET"])
def SelectCanales() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaCanales = canalDAO.SelectCanales()
        canalJ = {}
        for canal in listaCanales:
            canalJ[str(canal.idCanal)] = {

            "idCanal"       :canal.idCanal,
            "nomCanal"      :canal.nomCanal,
            "descripcion"   :canal.descripcion,
            "activo"        :canal.activo

            }
        
        respuesta["CanalJson"] = canalJ
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
# CANAL - GET por ID
# ============================================================
    
@canal_bp.route("/main/SelectCanalID/<int:idCanal>", methods=["GET"])
def SelectCanalID(idCanal: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        canal = canalDAO.SelectCanalId(idCanal)
        
        if canal: 
            respuesta["Entidad"] = {
            "idCanal"       :canal.idCanal,
            "nomCanal"      :canal.nomCanal,
            "descripcion"   :canal.descripcion,
            "activo"        :canal.activo
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
# CANAL - POST (INSERT)
# ============================================================

@canal_bp.route("/main/InsertCanal", methods=["POST"])
def InsertCanal() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevocanal = Canales()

        nuevocanal.nomCanal     =  datos ["nomCanal"]      
        nuevocanal.descripcion  =  datos  ["descripcion"]   
        nuevocanal.activo       =  datos ["activo"]


        canalDAO.InsertCanal(nuevocanal)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CANAL - PUT (UPDATE)
# ============================================================
    
@canal_bp.route("/main/UpdateCanal", methods=["PUT"])
def UpdateCanal() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarcanal   = Canales()

        actualizarcanal.idCanal      =  datos ["idCanal"] 
        actualizarcanal.nomCanal     =  datos ["nomCanal"]      
        actualizarcanal.descripcion  =  datos  ["descripcion"]   
        actualizarcanal.activo       =  datos ["activo"]
       

        canalDAO.UpdateCanal(actualizarcanal)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CANAL - DELETE (DELETE)
# ============================================================

@canal_bp.route("/main/DeleteCanal/<int:idCanal>", methods=["DELETE"])
def DeleteCanal(idCanal: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        canalDAO.DeleteCanal(idCanal)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)