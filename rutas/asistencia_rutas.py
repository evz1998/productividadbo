import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.asistencia_dao import AsistenciaDAO
from modelos.asistencia_modelo import Asistencia

# ============================================================
# BLUEPRINT - ASISTENCIA
# ============================================================

asistencia_bp = flask.Blueprint("asistencia",__name__)

con = Conexion()
asistenciaDAO = AsistenciaDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# ASISTENCIA - GET todas
# ============================================================

@asistencia_bp.route("/main/SelectAsistencias", methods=["GET"])
def SelectAsistencia() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaAsistencia = asistenciaDAO.SelectAsistencias()
        asistenciaJ = {}
        for asistencia in listaAsistencia:
            asistenciaJ[str(asistencia.idAsistencia)] = {

            "idAsistencia"      :asistencia.idAsistencia,
            "idAsesor"          :asistencia.idAsesor,
            "idTurno"           :asistencia.idTurno,
            "fecha"             :asistencia.fecha,
            "horaEntrada"       :asistencia.horaEntrada,
            "horaSalida"        :asistencia.horaSalida,
            "minutosTrabajados" :asistencia.minutosTrabajados

            }
        
        respuesta["AsistenciaJson"] = asistenciaJ
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
# ASISTENCIA - GET por ID
# ============================================================
    
@asistencia_bp.route("/main/SelectAsistenciaID/<int:idAsistencia>", methods=["GET"])
def SelectAsistenciaID(idAsistencia: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        asistencia = asistenciaDAO.SelectAsistenciaId(idAsistencia)
        
        if asistencia: 
            respuesta["Entidad"] = {
            "idAsistencia"      :asistencia.idAsistencia,
            "idAsesor"          :asistencia.idAsesor,
            "idTurno"           :asistencia.idTurno,
            "fecha"             :asistencia.fecha,
            "horaEntrada"       :asistencia.horaEntrada,
            "horaSalida"        :asistencia.horaSalida,
            "minutosTrabajados" :asistencia.minutosTrabajados
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
# ASISTENCIA - POST (INSERT)
# ============================================================

@asistencia_bp.route("/main/InsertAsistencia", methods=["POST"])
def InsertAsistencia() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevoasitencia = Asistencia()

        nuevoasitencia.idAsesor              = datos ["idAsesor"]
        nuevoasitencia.idTurno               = datos ["idTurno"]
        nuevoasitencia.fecha                 = datos ["fecha"]
        nuevoasitencia.horaEntrada           = datos ["horaEntrada"]
        nuevoasitencia.horaSalida            = datos ["horaSalida"]
        nuevoasitencia.minutosTrabajados     = datos ["minutosTrabajados"]

        asistenciaDAO.InsertAsistencia(nuevoasitencia)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)

# ============================================================
# ASISTENCIA - PUT
# ============================================================
    
@asistencia_bp.route("/main/UpdateAsistencia", methods=["PUT"])
def UpdateAsistencia() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarasistencia   = Asistencia()

        actualizarasistencia.idAsistencia          = datos ["idAsistencia"]
        actualizarasistencia.idAsesor              = datos ["idAsesor"]
        actualizarasistencia.idTurno               = datos ["idTurno"]
        actualizarasistencia.fecha                 = datos ["fecha"]
        actualizarasistencia.horaEntrada           = datos ["horaEntrada"]
        actualizarasistencia.horaSalida            = datos ["horaSalida"]
        actualizarasistencia.minutosTrabajados     = datos ["minutosTrabajados"]

        asistenciaDAO.UpdateAsistencia(actualizarasistencia)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# ASISTENCIA - DELETE
# ============================================================

@asistencia_bp.route("/main/DeleteAsistencia/<int:idAsistencia>", methods=["DELETE"])
def DeleteAsistencia(idAsistencia: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        asistenciaDAO.DeleteAsistencia(idAsistencia)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)