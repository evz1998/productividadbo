#Librerias
import datetime;
from modelos.areas_modelo import (Areas)
from modelos.cargos_modelo import (Cargos)

# ------------------------------------------------------------
# Clase: Asesores
# Representa un asesor del backoffice
# ------------------------------------------------------------
class Asesores:

    # Referencias a otras clases (objetos relacionados)
    _area:  Areas  = None;
    _cargo: Cargos = None;

    # Atributos
    idAsesor:     int      = 0;
    cedula:       str      = "";
    nombre:       str      = "";
    email:        str      = "";
    telefono:     str      = "";
    idArea:       int      = 0;
    idCargo:      int      = 0;
    fechaIngreso: datetime = None;
    activo:       bool     = False;

    # Propiedades / Métodos
    def GetIdAsesor(self) -> int:
        return self.idAsesor;
    def SetIdAsesor(self, valor: int) -> None:
        self.idAsesor = valor;

    def GetCedula(self) -> str:
        return self.cedula;
    def SetCedula(self, valor: str) -> None:
        self.cedula = valor;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, valor: str) -> None:
        self.nombre = valor;

    def GetEmail(self) -> str:
        return self.email;
    def SetEmail(self, valor: str) -> None:
        self.email = valor;

    def GetTelefono(self) -> str:
        return self.telefono;
    def SetTelefono(self, valor: str) -> None:
        self.telefono = valor;

    def GetActivo(self) -> bool:
        return self.activo;
    def SetActivo(self, valor: bool) -> None:
        self.activo = valor;