import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.asesores_dao import AsesoresDAO
from modelos.asesores_modelo import Asesores

# ============================================================
# BLUEPRINT - ASESORES
# ============================================================

asesores_bp = flask.Blueprint("asesores",__name__)

con = Conexion()
asesoresDAO = AsesoresDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# ASESORES - GET todas
# ============================================================

@asesores_bp.route("/main/SelectAsesores", methods=["GET"])
def SelectAsesores() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaAsesor = asesoresDAO.SelectAsesores()
        asesorJ = {}
        for asesor in listaAsesor:
            asesorJ[str(asesor.idAsesor)] = {

            "idAsesor"          :asesor.idAsesor,
            "cedula"            :asesor.cedula,
            "nombre"            :asesor.nombre,
            "email"             :asesor.email,
            "telefono"          :asesor.telefono,
            "idArea"            :asesor.idArea,
            "idCargo"           :asesor.idCargo,
            "fechaIngreso"      :asesor.fechaIngreso,
            "activo"            :asesor.activo  
            }
        
        respuesta["AsesorJson"] = asesorJ
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
# ASESORES - GET por ID
# ============================================================
    
@asesores_bp.route("/main/SelectAsesorID/<int:idAsesor>", methods=["GET"])
def SelectAsesorID(idAsesor: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        asesor = asesoresDAO.SelectAsesorId(idAsesor)
        
        if asesor: 
            respuesta["Entidad"] = {
            "idAsesor"          :asesor.idAsesor,
            "cedula"            :asesor.cedula,
            "nombre"            :asesor.nombre,
            "email"             :asesor.email,
            "telefono"          :asesor.telefono,
            "idArea"            :asesor.idArea,
            "idCargo"           :asesor.idCargo,
            "fechaIngreso"      :asesor.fechaIngreso,
            "activo"            :asesor.activo 
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
# ASESORES - POST (INSERT)
# ============================================================

@asesores_bp.route("/main/InsertAsesor", methods=["POST"])
def InsertAsesor() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoasesor = Asesores()
        nuevoasesor.cedula           = datos ["cedula"]
        nuevoasesor.nombre           = datos ["nombre"]
        nuevoasesor.email            = datos ["email"]
        nuevoasesor.telefono         = datos ["telefono"]
        nuevoasesor.idArea           = datos ["idArea"]
        nuevoasesor.idCargo          = datos ["idCargo"]
        nuevoasesor.fechaIngreso     = datos ["fechaIngreso"]
        nuevoasesor.activo           = datos ["activo"]

        asesoresDAO.InsertAsesor(nuevoasesor)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# ASESORES - PUT Update
# ============================================================

@asesores_bp.route("/main/UpdateAsesor", methods=["PUT"])
def UpdateAsesor() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarasesor               = Asesores()

        actualizarasesor.idAsesor         = datos ["idAsesor"]
        actualizarasesor.cedula           = datos ["cedula"]
        actualizarasesor.nombre           = datos ["nombre"]
        actualizarasesor.email            = datos ["email"]
        actualizarasesor.telefono         = datos ["telefono"]
        actualizarasesor.idArea           = datos ["idArea"]
        actualizarasesor.idCargo          = datos ["idCargo"]
        actualizarasesor.fechaIngreso     = datos ["fechaIngreso"]
        actualizarasesor.activo           = datos ["activo"]

        asesoresDAO.UpdateAsesor(actualizarasesor)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# ASESORES - DELETE
# ============================================================

@asesores_bp.route("/main/DeleteAsesor/<int:idAsesor>", methods=["DELETE"])
def DeleteAsesor(idAsesor: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        asesoresDAO.DeleteAsesor(idAsesor)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)