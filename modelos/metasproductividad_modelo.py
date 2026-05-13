#Librerias
import datetime;

from modelos.areas_modelo import (Areas)
from modelos.tiposcaso_modelo import (TiposCaso)

# ------------------------------------------------------------
# Clase: MetasProductividad
# Metas de productividad definidas por área y tipo de caso
# ------------------------------------------------------------
class MetasProductividad:

    # Referencias a otras clases (objetos relacionados)
    _area:     Areas     = None;
    _tipoCaso: TiposCaso = None;

    # Atributos
    idMeta:        int      = 0;
    idArea:        int      = 0;
    idTipoCaso:    int      = 0;
    casosMetaDia:  int      = 0;
    vigenciaDesde: datetime = datetime.datetime.now();
    vigenciaHasta: datetime = datetime.datetime.now();
    activa:        bool     = False;

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdMeta(self) -> int:
        return self.idMeta;
    def SetIdMeta(self, valor: int) -> None:
        self.idMeta = valor;

    def GetCasosMetaDia(self) -> int:
        return self.casosMetaDia;
    def SetCasosMetaDia(self, valor: int) -> None:
        self.casosMetaDia = valor;

    def GetActiva(self) -> bool:
        return self.activa;
    def SetActiva(self, valor: bool) -> None:
        self.activa = valor;