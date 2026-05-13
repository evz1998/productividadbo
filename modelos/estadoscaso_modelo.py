# ------------------------------------------------------------
# Clase: estadosCaso
# Representa los estados por los que puede pasar un caso
# ------------------------------------------------------------
class estadosCaso:

    # Atributos
    idEstado:    int  = 0;
    nomEstado:   str  = "";
    descripcion: str  = "";
    esfinal:     bool = False;
    activo:      bool = False;

    # Propiedades / Métodos
    def GetIdEstado(self) -> int:
        return self.idEstado;
    def SetIdEstado(self, valor: int) -> None:
        self.idEstado = valor;

    def GetNomEstado(self) -> str:
        return self.nomEstado;
    def SetNomEstado(self, valor: str) -> None:
        self.nomEstado = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;

    def GetEsFinal(self) -> bool:
        return self.esfinal;
    def SetEsFinal(self, valor: bool) -> None:
        self.esfinal = valor;

    def GetActivo(self) -> bool:
        return self.activo;
    def SetActivo(self, valor: bool) -> None:
        self.activo = valor;
