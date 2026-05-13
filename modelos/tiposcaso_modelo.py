
# ------------------------------------------------------------
# Clase: TiposCaso
# Representa un tipo de caso que pueden gestionar los asesores
# ------------------------------------------------------------
class TiposCaso:

    # Atributos
    idTipoCaso:  int  = 0;
    nomTipo:     str  = "";
    descripcion: str  = "";
    tiempoMeta:  int  = 0;
    activo:      bool = False;

    # Propiedades / Métodos
    def GetIdTipoCaso(self) -> int:
        return self.idTipoCaso;
    def SetIdTipoCaso(self, valor: int) -> None:
        self.idTipoCaso = valor;

    def GetNomTipo(self) -> str:
        return self.nomTipo;
    def SetNomTipo(self, valor: str) -> None:
        self.nomTipo = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;

    def GetTiempoMeta(self) -> int:
        return self.tiempoMeta;
    def SetTiempoMeta(self, valor: int) -> None:
        self.tiempoMeta = valor;  # Corregido: antes asignaba self.idTipoCaso

    def GetActivo(self) -> bool:
        return self.activo;
    def SetActivo(self, valor: bool) -> None:
        self.activo = valor;
