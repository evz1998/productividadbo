import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.turnos_dao import TurnosDAO
from modelos.turnos_modelo import Turnos

# ============================================================
# BLUEPRINT - TURNOS
# ============================================================

turnos_bp = flask.Blueprint("turnos",__name__)

con = Conexion()
turnosDAO = TurnosDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# TURNOS - GET todas
# ============================================================

@turnos_bp.route("/main/SelectTurnos", methods=["GET"])
def SelectTurnos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaTurno = turnosDAO.SelectTurnos()
        turnoJ = {}
        for turno in listaTurno:
            turnoJ[str(turno.idTurno)] = {

            "idTurno"           :turno.idTurno,
            "nomturno"          :turno.nomturno,
            "horaInicio"        :turno.horaInicio,
            "horaFin"           :turno.horaFin,
            "activo"            :turno.activo

            }
        
        respuesta["TurnoJson"] = turnoJ
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
# TURNOS - GET por ID
# ============================================================
    
@turnos_bp.route("/main/SelectTurnosID/<int:idTurno>", methods=["GET"])
def SelectTurnosID(idTurno: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        turno = turnosDAO.SelectTurnoId(idTurno)
        
        if turno: 
            respuesta["Entidad"] = {
        
            "idTurno"           :turno.idTurno,
            "nomturno"          :turno.nomturno,
            "horaInicio"        :turno.horaInicio,
            "horaFin"           :turno.horaFin,
            "activo"            :turno.activo

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
# TURNOS - POST (INSERT)
# ============================================================

@turnos_bp.route("/main/InsertTurnos", methods=["POST"])
def InsertTurnos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoturno               = Turnos()

        nuevoturno.nomturno       = datos ["nomturno"]
        nuevoturno.horaInicio     = datos ["horaInicio"]
        nuevoturno.horaFin        = datos ["horaFin"]
        nuevoturno.activo         = datos ["activo"]

        turnosDAO.InsertTurno(nuevoturno)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# TURNOS - PUT (UPDATE)
# ============================================================
    
@turnos_bp.route("/main/UpdateTurnos", methods=["PUT"])
def UpdateTurnos() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarturno               = Turnos()

        actualizarturno.idTurno        = datos ["idTurno"]
        actualizarturno.nomturno       = datos ["nomturno"]
        actualizarturno.horaInicio     = datos ["horaInicio"]
        actualizarturno.horaFin        = datos ["horaFin"]
        actualizarturno.activo         = datos ["activo"]
        
        turnosDAO.UpdateTurno(actualizarturno)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# TURNOS - DELETE 
# ============================================================

@turnos_bp.route("/main/DeleteTurno/<int:idTurno>", methods=["DELETE"])
def DeleteTurno(idTurno: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        turnosDAO.DeleteTurno(idTurno)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)