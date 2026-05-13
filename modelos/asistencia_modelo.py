#Librerias
import datetime;

from modelos.asesores_modelo import (Asesores)
from modelos.turnos_modelo import (Turnos)

# ------------------------------------------------------------
# Clase: Asistencia
# Registro de asistencia diaria de cada asesor
# ------------------------------------------------------------
class Asistencia:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores = None;
    _turno:  Turnos   = None;

    # Atributos
    idAsistencia:      int      = 0;
    idAsesor:          int      = 0;
    idTurno:           int      = 0;
    fecha:             datetime = datetime.datetime.now();
    horaEntrada:       datetime = datetime.datetime.now();
    horaSalida:        datetime = datetime.datetime.now();
    minutosTrabajados: int      = 0;

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdAsistencia(self) -> int:
        return self.idAsistencia;
    def SetIdAsistencia(self, valor: int) -> None:
        self.idAsistencia = valor;

    def GetMinutosTrabajados(self) -> int:
        return self.minutosTrabajados;
    def SetMinutosTrabajados(self, valor: int) -> None:
        self.minutosTrabajados = valor;