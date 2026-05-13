#Librerias
import datetime;

from modelos.clientes_modelo import (Clientes)
from modelos.tiposcaso_modelo import (TiposCaso)
from modelos.prioridades_modelo import (Prioridades)
from modelos.canales_modelo import (Canales)
from modelos.estadoscaso_modelo import (estadosCaso)
from modelos.asesores_modelo import (Asesores)


# ------------------------------------------------------------
# Clase: Casos
# Tabla central: casos gestionados por los asesores
# ------------------------------------------------------------
class Casos:

    # Referencias a otras clases (objetos relacionados)
    _cliente:   Clientes    = None;
    _tipoCaso:  TiposCaso   = None;  # Corregido: antes decía Casos (se referenciaba a sí misma)
    _prioridad: Prioridades = None;
    _canal:     Canales     = None;
    _estado:    estadosCaso = None;
    _asesor:    Asesores    = None;

    # Atributos
    idCaso:        int      = 0;
    idCliente:     int      = 0;
    idTipoCaso:    int      = 0;
    idPrioridad:   int      = 0;
    idCanal:       int      = 0;
    idEstado:      int      = 0;
    idAsesor:      int      = 0;
    descripcion:   str      = "";
    fechaApertura: datetime = datetime.datetime.now();
    fechaCierre:   datetime = datetime.datetime.now();

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdCaso(self) -> int:
        return self.idCaso;
    def SetIdCaso(self, valor: int) -> None:
        self.idCaso = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;
