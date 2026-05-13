import flask;
import sys;


from conexion.token import generarToken;
from rutas.areas_rutas import areas_bp;
from rutas.asesores_rutas import asesores_bp;
from rutas.asistencia_rutas import asistencia_bp;
from rutas.canales_rutas import canal_bp;
from rutas.cargos_rutas import cargos_bp;
from rutas.casos_rutas import casos_bp;
from rutas.clientes_rutas import cliente_bp;
from rutas.estadoscaso_rutas import estadocaso_bp;
from rutas.evaluaciones_rutas import evaluaciones_bp;
from rutas.metasproductividad_rutas import metasproductividad_bp;
from rutas.prioridades_rutas import prioridad_bp;
from rutas.reportesdiarios_rutas import reportediario_bp;
from rutas.seguimientocasos_rutas import seguimientocasos_bp;
from rutas.tiposcaso_rutas import tiposcasos_bp;
from rutas.turnos_rutas import turnos_bp;


# ============================================================
# INICIALIZAR APP
# ============================================================
print("API Backoffice - Sistema de Productividad");
app = flask.Flask(__name__);

# ============================================================
# REGISTRAR BLUEPRINTS
# ============================================================
app.register_blueprint(areas_bp);
app.register_blueprint(asesores_bp);
app.register_blueprint(asistencia_bp);
app.register_blueprint(canal_bp);
app.register_blueprint(cargos_bp);
app.register_blueprint(casos_bp);
app.register_blueprint(cliente_bp);
app.register_blueprint(estadocaso_bp);
app.register_blueprint(evaluaciones_bp);
app.register_blueprint(metasproductividad_bp);
app.register_blueprint(prioridad_bp);
app.register_blueprint(reportediario_bp);
app.register_blueprint(seguimientocasos_bp);
app.register_blueprint(tiposcasos_bp);
app.register_blueprint(turnos_bp);

# ============================================================
# ENDPOINT: OBTENER TOKEN (no requiere autenticación)
# GET http://localhost:4040/main/ObtenerToken
# ============================================================

@app.route("/main/ObtenerToken", methods=["GET"])
def ObtenerToken():
    respuesta: dict = {};
    try:
        token = generarToken();
        respuesta["Respuesta"] = "OK";
        respuesta["Token"]     = token;
        return flask.jsonify(respuesta);
    except:
        respuesta["Respuesta"] = "ERROR";
        respuesta["Mensaje"]   = str(sys.exc_info());
        return flask.jsonify(respuesta);

app.run("localhost", 4040, debug=True)