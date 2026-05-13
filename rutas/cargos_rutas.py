import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.cargos_dao import CargosDAO
from modelos.cargos_modelo import Cargos

# ============================================================
# BLUEPRINT - CARGOS
# ============================================================

cargos_bp = flask.Blueprint("cargos",__name__)

con = Conexion()
cargosDAO = CargosDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# CARGOS - GET todas
# ============================================================

@cargos_bp.route("/main/SelectCargos", methods=["GET"])
def SelectCargos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaCargo = cargosDAO.SelectCargos()
        cargoJ = {}
        for cargo in listaCargo:
            cargoJ[str(cargo.idCargo)] = {

                "idCargo"       :cargo.idCargo,
                "nomCargo"      :cargo.nomCargo,
                "nivel"         :cargo.nivel,
                "activo"        :cargo.activo
            }
        
        respuesta["CargoJson"] = cargoJ
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
# CARGOS - GET por ID
# ============================================================
    
@cargos_bp.route("/main/SelectCargoID/<int:idCargo>", methods=["GET"])
def SelectCargoID(idCargo: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        cargo = cargosDAO.SelectCargoId(idCargo)
        
        if cargo: 
            respuesta["Entidad"] = {
                "idCargo"       :cargo.idCargo,
                "nomCargo"      :cargo.nomCargo,
                "nivel"         :cargo.nivel,
                "activo"        :cargo.activo
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
# CARGOS - POST (INSERT)
# ============================================================

@cargos_bp.route("/main/InsertCargo", methods=["POST"])
def InsertCargo() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevocargo              = Cargos()
        nuevocargo.nomCargo     = datos ["nomCargo"]
        nuevocargo.nivel        = datos ["nivel"]
        nuevocargo.activo       = datos ["activo"]

        cargosDAO.InsertCargo(nuevocargo)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CARGOS - PUT (UPDATE)
# ============================================================
    
@cargos_bp.route("/main/UpdateCargo", methods=["PUT"])
def UpdateCargo() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarcargo                = Cargos()

        actualizarcargo.idCargo       = datos ["idCargo"]
        actualizarcargo.nomCargo      = datos ["nomCargo"]
        actualizarcargo.nivel         = datos ["nivel"]
        actualizarcargo.activo        = datos ["activo"]

        cargosDAO.UpdateCargo(actualizarcargo)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)

# ============================================================
# CARGOS - DELETE 
# ============================================================

@cargos_bp.route("/main/DeleteCargo/<int:idCargo>", methods=["DELETE"])
def DeleteCargo(idCargo: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        cargosDAO.DeleteCargo(idCargo)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)