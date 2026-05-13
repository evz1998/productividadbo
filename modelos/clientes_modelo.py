#Librerias
import datetime;

# ------------------------------------------------------------
# Clase: Clientes
# Representa un cliente o usuario que genera los casos
# ------------------------------------------------------------
class Clientes:

    # Atributos
    idCliente:     int      = 0;
    documento:     str      = "";
    nombre:        str      = "";
    email:         str      = "";
    telefono:      str      = "";
    fechaRegistro: datetime = None;
    activo:        bool     = False;

    # Propiedades / Métodos
    def GetIdCliente(self) -> int:
        return self.idCliente;
    def SetIdCliente(self, valor: int) -> None:
        self.idCliente = valor;

    def GetDocumento(self) -> str:
        return self.documento;
    def SetDocumento(self, valor: str) -> None:
        self.documento = valor;

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