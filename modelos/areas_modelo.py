# ------------------------------------------------------------
# Clase: Areas
# Representa un área o departamento de la empresa
# ------------------------------------------------------------
class Areas:

    # Atributos
    idArea:      int  = 0;
    nomArea:     str  = "";
    descripcion: str  = "";
    activa:      bool = False;

    # Propiedades / Métodos
    def GetIDArea(self) -> int:
        return self.idArea;
    def SetIDArea(self, valor: int) -> None:
        self.idArea = valor;

    def GetNomArea(self) -> str:
        return self.nomArea;
    def SetNomArea(self, valor: str) -> None:
        self.nomArea = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;

    def GetActiva(self) -> bool:
        return self.activa;
    def SetActiva(self, valor: bool) -> None:
        self.activa = valor;