#Librerias
import datetime;
from modelos.asesores_modelo import (Asesores)

# ------------------------------------------------------------
# Clase: ReportesDiarios
# Resumen consolidado de productividad por asesor y día
# ------------------------------------------------------------
class ReportesDiarios:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores = None;

    # Atributos
    idReporte:      int      = 0;
    idAsesor:       int      = 0;
    fecha:          datetime = datetime.datetime.now();
    casosAbiertos:  int      = 0;
    casosCerrados:  int      = 0;
    casosEnProceso: int      = 0;
    tiempoPromedio: float    = 0.0;
    cumplioMeta:    bool     = False;

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdReporte(self) -> int:
        return self.idReporte;
    def SetIdReporte(self, valor: int) -> None:
        self.idReporte = valor;

    def GetCumplioMeta(self) -> bool:
        return self.cumplioMeta;
    def SetCumplioMeta(self, valor: bool) -> None:
        self.cumplioMeta = valor;

    def GetCasosCerrados(self) -> int:
        return self.casosCerrados;
    def SetCasosCerrados(self, valor: int) -> None:
        self.casosCerrados = valor;
