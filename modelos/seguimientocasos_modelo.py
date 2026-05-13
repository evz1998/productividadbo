#Librerias
import datetime;
from modelos.estadoscaso_modelo import (estadosCaso)
from modelos.casos_modelo import (Casos)
from modelos.asesores_modelo import (Asesores)

# ------------------------------------------------------------
# Clase: seguimientoCasos
# Historial de cambios de estado y notas en cada caso
# ------------------------------------------------------------
class seguimientoCasos:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores    = None;
    _caso:   Casos       = None;
    _estado: estadosCaso = None;

    # Atributos
    idSeguimiento: int      = 0;
    idCaso:        int      = 0;
    idAsesor:      int      = 0;
    idEstado:      int      = 0;
    nota:          str      = "";
    fecharegistro: datetime = datetime.datetime.now();

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdSeguimiento(self) -> int:
        return self.idSeguimiento;
    def SetIdSeguimiento(self, valor: int) -> None:
        self.idSeguimiento = valor;

    def GetNota(self) -> str:
        return self.nota;
    def SetNota(self, valor: str) -> None:
        self.nota = valor;
