# ------------------------------------------------------------
# Clase: Cargos
# Representa un cargo o rol que puede tener un asesor
# ------------------------------------------------------------
class Cargos:

    # Atributos
    idCargo:  int  = 0;
    nomCargo: str  = "";
    nivel:    int  = 0;
    activo:   bool = False;

    # Propiedades / Métodos
    def GetIDCargo(self) -> int:
        return self.idCargo;
    def SetIDCargo(self, valor: int) -> None:
        self.idCargo = valor;

    def GetNomCargo(self) -> str:
        return self.nomCargo;
    def SetNomCargo(self, valor: str) -> None:
        self.nomCargo = valor;

    def GetNivel(self) -> int:
        return self.nivel;
    def SetNivel(self, valor: int) -> None:
        self.nivel = valor;

    def GetActivo(self) -> bool:
        return self.activo;
    def SetActivo(self, valor: bool) -> None:
        self.activo = valor;