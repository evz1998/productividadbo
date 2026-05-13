#Librerias
import datetime;
from modelos.asesores_modelo import (Asesores)

# ------------------------------------------------------------
# Clase: Evaluaciones
# Evaluaciones de desempeño de los asesores
# ------------------------------------------------------------
class Evaluaciones:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores = None;

    # Atributos
    idEvaluacion:     int      = 0;
    idAsesor:         int      = 0;
    periodo:          str      = "";
    calidad:          float    = 0.0;
    puntualidad:      float    = 0.0;
    casosGestionados: int      = 0;
    nota:             float    = 0.0;
    fechaEvaluacion:  datetime = datetime.datetime.now();

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdEvaluacion(self) -> int:
        return self.idEvaluacion;
    def SetIdEvaluacion(self, valor: int) -> None:
        self.idEvaluacion = valor;

    def GetNota(self) -> float:
        return self.nota;
    def SetNota(self, valor: float) -> None:
        self.nota = valor;

    def GetCasosGestionados(self) -> int:
        return self.casosGestionados;
    def SetCasosGestionados(self, valor: int) -> None:
        self.casosGestionados = valor;