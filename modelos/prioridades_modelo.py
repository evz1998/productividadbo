# ------------------------------------------------------------
# Clase: Prioridades
# Representa los niveles de prioridad de un caso
# ------------------------------------------------------------
class Prioridades:

    # Atributos
    idPrioridad:  int  = 0;
    nomPrioridad: str  = "";
    nivel:        int  = 0;
    activa:       bool = False;

    # Propiedades / Métodos
    def GetIdPrioridad(self) -> int:
        return self.idPrioridad;
    def SetIdPrioridad(self, valor: int) -> None:
        self.idPrioridad = valor;

    def GetNomPrioridad(self) -> str:
        return self.nomPrioridad;
    def SetNomPrioridad(self, valor: str) -> None:
        self.nomPrioridad = valor;

    def GetNivel(self) -> int:
        return self.nivel;
    def SetNivel(self, valor: int) -> None:
        self.nivel = valor;

    def GetActiva(self) -> bool:
        return self.activa;
    def SetActiva(self, valor: bool) -> None:
        self.activa = valor;
