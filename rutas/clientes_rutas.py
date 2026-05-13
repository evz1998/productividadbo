import flask
import json
import sys
import datetime
import decimal

from conexion.conexion import Conexion
from conexion.token import validarToken
from daos.clientes_dao import ClientesDAO
from modelos.clientes_modelo import Clientes

# ============================================================
# BLUEPRINT - CLIENTES
# ============================================================

cliente_bp = flask.Blueprint("cliente",__name__)

con = Conexion()
clienteDAO = ClientesDAO(con)

def convertir(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    return str(obj)

# ============================================================
# CLIENTES - GET todas
# ============================================================

@cliente_bp.route("/main/SelectClientes", methods=["GET"])
def SelectClientes() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        listaCliente = clienteDAO.SelectClientes()
        clienteJ = {}
        for cliente in listaCliente:
            clienteJ[str(cliente.idCliente)] = {

            "idCliente"          :cliente.idCliente,
            "documento"          :cliente.documento,
            "nombre"             :cliente.nombre,
            "email"              :cliente.email,
            "telefono"           :cliente.telefono,
            "fechaRegistro"      :cliente.fechaRegistro,
            "activo"             :cliente.activo

            }
        
        respuesta["ClienteJson"] = clienteJ
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
# CLIENTES - GET por ID
# ============================================================
    
@cliente_bp.route("/main/SelectClienteID/<int:idCliente>", methods=["GET"])
def SelectClienteID(idCliente: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        cliente = clienteDAO.SelectClienteId(idCliente)
        
        if cliente: 
            respuesta["Entidad"] = {

            "idCliente"          :cliente.idCliente,
            "documento"          :cliente.documento,
            "nombre"             :cliente.nombre,
            "email"              :cliente.email,
            "telefono"           :cliente.telefono,
            "fechaRegistro"      :cliente.fechaRegistro,
            "activo"             :cliente.activo    

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
# CLIENTES - POST (INSERT)
# ============================================================

@cliente_bp.route("/main/InsertClientes", methods=["POST"])
def InsertClientes() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        nuevocliente               = Clientes()  

        nuevocliente.documento       = datos ["documento"]
        nuevocliente.nombre          = datos ["nombre"]
        nuevocliente.email           = datos ["email"]
        nuevocliente.telefono        = datos ["telefono"]
        nuevocliente.fechaRegistro   = datos ["fechaRegistro"]
        nuevocliente.activo          = datos ["activo"]

        clienteDAO.InsertCliente(nuevocliente)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CLIENTES - PUT (UPDATE)
# ============================================================
    
@cliente_bp.route("/main/UpdateCliente", methods=["PUT"])
def UpdateCliente() -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
        
        datos = flask.request.get_json()
       
        actualizarcliente              = Clientes()
    
        actualizarcliente.idCliente       = datos ["idCliente"]
        actualizarcliente.documento       = datos ["documento"]
        actualizarcliente.nombre          = datos ["nombre"]
        actualizarcliente.email           = datos ["email"]
        actualizarcliente.telefono        = datos ["telefono"]
        actualizarcliente.fechaRegistro   = datos ["fechaRegistro"]
        actualizarcliente.activo          = datos ["activo"]

        clienteDAO.UpdateCliente(actualizarcliente)

        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)
    
# ============================================================
# CLIENTE - DELETE 
# ============================================================

@cliente_bp.route("/main/DeleteCliente/<int:idCliente>", methods=["DELETE"])
def DeleteCliente(idCliente: int) -> str:
    respuesta: dict = {}
    try:
        if not validarToken():
            respuesta["Error"] ="NoAuthentication"
            return flask.jsonify(respuesta)
    
        clienteDAO.DeleteCliente(idCliente)
        respuesta["Respuesta"] = "OK"
        return flask.jsonify(respuesta)
    
    except:
        respuesta ["Respuesta"] = "ERROR"
        respuesta ["Mensaje"] = str(sys.exc_info())
        return flask.jsonify(respuesta)