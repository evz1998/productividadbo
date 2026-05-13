#Librerias
import datetime;
# ------------------------------------------------------------
# Clase: Turnos
# Representa los turnos de trabajo de los asesores
# ------------------------------------------------------------
class Turnos:

    # Atributos
    idTurno:    int      = 0;
    nomturno:   str      = "";
    horaInicio: datetime = datetime.datetime.now();
    horaFin:    datetime = datetime.datetime.now();
    activo:     bool     = False;

    # Propiedades / Métodos
    def GetIdTurno(self) -> int:
        return self.idTurno;
    def SetIdTurno(self, valor: int) -> None:
        self.idTurno = valor;

    def GetNomTurno(self) -> str:
        return self.nomturno;
    def SetNomTurno(self, valor: str) -> None:
        self.nomturno = valor;