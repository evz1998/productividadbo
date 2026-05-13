# ------------------------------------------------------------
# Clase: Canales
# Representa el canal por el que llega un caso (email, chat...)
# ------------------------------------------------------------
class Canales:

    # Atributos
    idCanal:     int  = 0;
    nomCanal:    str  = "";
    descripcion: str  = "";
    activo:      bool = False;

    # Propiedades / Métodos
    def GetIdCanal(self) -> int:
        return self.idCanal;
    def SetIdCanal(self, valor: int) -> None:
        self.idCanal = valor;

    def GetNomCanal(self) -> str:
        return self.nomCanal;
    def SetNomCanal(self, valor: str) -> None:
        self.nomCanal = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;

    def GetActivo(self) -> bool:
        return self.activo;
    def SetActivo(self, valor: bool) -> None:
        self.activo = valor;
