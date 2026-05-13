import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.metasproductividad_dao import MetasProductividadDAO
from modelos.metasproductividad_modelo import MetasProductividad

# ============================================================
# BLUEPRINT - METAS PRODUCTIVIDAD
# ============================================================

metasproductividad_bp = flask.Blueprint("metasproductividad",__name__)

con = Conexion()
metasproductividadDAO = MetasProductividadDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# METAS PRODUCTIVIDAD - GET todas
# ============================================================

@metasproductividad_bp.route("/main/SelectMetasProductividad", methods=["GET"])
def SelectMetasProductividad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaMetasProductividad = metasproductividadDAO.SelectMetasProductividad()
        metaproductividadJ = {}
        for metaproductividad in listaMetasProductividad:
            metaproductividadJ[str(metaproductividad.idMeta)] = {


            "idMeta"                :metaproductividad.idMeta,
            "idArea"                :metaproductividad.idArea,
            "idTipoCaso"            :metaproductividad.idTipoCaso,
            "casosMetaDia"          :metaproductividad.casosMetaDia,
            "vigenciaDesde"         :metaproductividad.vigenciaDesde,
            "vigenciaHasta"         :metaproductividad.vigenciaHasta,
            "activa"                :metaproductividad.activa

            }
        
        respuesta["MetaPJson"] = metaproductividadJ
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
# META PRODUCTIVIDADAD - GET por ID
# ============================================================
    
@metasproductividad_bp.route("/main/SelectMetaProductividadID/<int:idMeta>", methods=["GET"])
def SelectMetaProductividadID(idMeta: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        metaproductividad = metasproductividadDAO.SelectMetaProductividadId(idMeta)
        
        if metaproductividad: 
            respuesta["Entidad"] = {
           
            "idMeta"                :metaproductividad.idMeta,
            "idArea"                :metaproductividad.idArea,
            "idTipoCaso"            :metaproductividad.idTipoCaso,
            "casosMetaDia"          :metaproductividad.casosMetaDia,
            "vigenciaDesde"         :metaproductividad.vigenciaDesde,
            "vigenciaHasta"         :metaproductividad.vigenciaHasta,
            "activa"                :metaproductividad.activa

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
# META PRODUCTIVIDAD - POST (INSERT)
# ============================================================

@metasproductividad_bp.route("/main/InsertMetaProductividad", methods=["POST"])
def InsertMetaProductividad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevameta           = MetasProductividad()  

        nuevameta.idMeta                = datos ["idMeta"]
        nuevameta.idArea                = datos ["idArea"]
        nuevameta.idTipoCaso            = datos ["idTipoCaso"]
        nuevameta.casosMetaDia          = datos ["casosMetaDia"]
        nuevameta.vigenciaDesde         = datos ["vigenciaDesde"]
        nuevameta.vigenciaHasta         = datos ["vigenciaHasta"]
        nuevameta.activa                = datos ["activa"]

        metasproductividadDAO.InsertMeta(nuevameta)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# META PRODUCTIVIDAD - PUT (UPDATE)
# ============================================================
    
@metasproductividad_bp.route("/main/UpdateMetaProductividad", methods=["PUT"])
def UpdateMetaProductividad() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarmeta                  = MetasProductividad()

        actualizarmeta.idMeta                = datos ["idMeta"]
        actualizarmeta.idArea                = datos ["idArea"]
        actualizarmeta.idTipoCaso            = datos ["idTipoCaso"]
        actualizarmeta.casosMetaDia          = datos ["casosMetaDia"]
        actualizarmeta.vigenciaDesde         = datos ["vigenciaDesde"]
        actualizarmeta.vigenciaHasta         = datos ["vigenciaHasta"]
        actualizarmeta.activa                = datos ["activa"]

        metasproductividadDAO.UpdateMetaProductividad(actualizarmeta)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# META PRODUCTIVIDAD - DELETE 
# ============================================================

@metasproductividad_bp.route("/main/DeleteMetaProductividad/<int:idMeta>", methods=["DELETE"])
def DeleteMetaProductividad(idMeta: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        metasproductividadDAO.DeleteMetaProductividad(idMeta)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)