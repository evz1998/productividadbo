# Librerias
import datetime;
import pyodbc;

# ============================================================
# CLASES ENTIDADES
# ============================================================

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
    fechaIngreso: datetime = datetime.datetime.now();
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
    fechaRegistro: datetime = datetime.datetime.now();
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

# ------------------------------------------------------------
# Clase: Casos
# Tabla central: casos gestionados por los asesores
# ------------------------------------------------------------
class Casos:

    # Referencias a otras clases (objetos relacionados)
    _cliente:   Clientes    = None;
    _tipoCaso:  TiposCaso   = None;  # Corregido: antes decía Casos (se referenciaba a sí misma)
    _prioridad: Prioridades = None;
    _canal:     Canales     = None;
    _estado:    estadosCaso = None;
    _asesor:    Asesores    = None;

    # Atributos
    idCaso:        int      = 0;
    idCliente:     int      = 0;
    idTipoCaso:    int      = 0;
    idPrioridad:   int      = 0;
    idCanal:       int      = 0;
    idEstado:      int      = 0;
    idAsesor:      int      = 0;
    descripcion:   str      = "";
    fechaApertura: datetime = datetime.datetime.now();
    fechaCierre:   datetime = datetime.datetime.now();

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdCaso(self) -> int:
        return self.idCaso;
    def SetIdCaso(self, valor: int) -> None:
        self.idCaso = valor;

    def GetDescripcion(self) -> str:
        return self.descripcion;
    def SetDescripcion(self, valor: str) -> None:
        self.descripcion = valor;

# ------------------------------------------------------------
# Clase: seguimientoCasos
# Historial de cambios de estado y notas en cada caso
# ------------------------------------------------------------
class seguimientoCasos:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores    = None;
    _caso:   Casos       = None;
    _estado: estadosCaso = None;

    # Atributos
    idSeguimiento: int      = 0;
    idCaso:        int      = 0;
    idAsesor:      int      = 0;
    idEstado:      int      = 0;
    nota:          str      = "";
    fecharegistro: datetime = datetime.datetime.now();  # Corregido: línea rota anterior

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdSeguimiento(self) -> int:
        return self.idSeguimiento;
    def SetIdSeguimiento(self, valor: int) -> None:
        self.idSeguimiento = valor;

    def GetNota(self) -> str:
        return self.nota;
    def SetNota(self, valor: str) -> None:
        self.nota = valor;

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

# ------------------------------------------------------------
# Clase: MetasProductividad
# Metas de productividad definidas por área y tipo de caso
# ------------------------------------------------------------
class MetasProductividad:

    # Referencias a otras clases (objetos relacionados)
    _area:     Areas     = None;
    _tipoCaso: TiposCaso = None;

    # Atributos
    idMeta:        int      = 0;
    idArea:        int      = 0;
    idTipoCaso:    int      = 0;
    casosMetaDia:  int      = 0;
    vigenciaDesde: datetime = datetime.datetime.now();
    vigenciaHasta: datetime = datetime.datetime.now();
    activa:        bool     = False;

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdMeta(self) -> int:
        return self.idMeta;
    def SetIdMeta(self, valor: int) -> None:
        self.idMeta = valor;

    def GetCasosMetaDia(self) -> int:
        return self.casosMetaDia;
    def SetCasosMetaDia(self, valor: int) -> None:
        self.casosMetaDia = valor;

    def GetActiva(self) -> bool:
        return self.activa;
    def SetActiva(self, valor: bool) -> None:
        self.activa = valor;

# ------------------------------------------------------------
# Clase: Evaluaciones
# Evaluaciones de desempeño de los asesores
# ------------------------------------------------------------
class Evaluaciones:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores = None;

    # Atributos
    idEvaluacion:     int      = 0;
    idAsesor:         int      = 0;
    periodo:          str      = "";
    calidad:          float    = 0.0;
    puntualidad:      float    = 0.0;
    casosGestionados: int      = 0;
    nota:             float    = 0.0;
    fechaEvaluacion:  datetime = datetime.datetime.now();

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdEvaluacion(self) -> int:
        return self.idEvaluacion;
    def SetIdEvaluacion(self, valor: int) -> None:
        self.idEvaluacion = valor;

    def GetNota(self) -> float:
        return self.nota;
    def SetNota(self, valor: float) -> None:
        self.nota = valor;

    def GetCasosGestionados(self) -> int:
        return self.casosGestionados;
    def SetCasosGestionados(self, valor: int) -> None:
        self.casosGestionados = valor;

# ------------------------------------------------------------
# Clase: ReportesDiarios
# Resumen consolidado de productividad por asesor y día
# ------------------------------------------------------------
class ReportesDiarios:

    # Referencias a otras clases (objetos relacionados)
    _asesor: Asesores = None;

    # Atributos
    idReporte:      int      = 0;
    idAsesor:       int      = 0;
    fecha:          datetime = datetime.datetime.now();
    casosAbiertos:  int      = 0;
    casosCerrados:  int      = 0;
    casosEnProceso: int      = 0;
    tiempoPromedio: float    = 0.0;
    cumplioMeta:    bool     = False;

    # Constructor
    def __init__(self):
        pass;

    # Propiedades / Métodos
    def GetIdReporte(self) -> int:
        return self.idReporte;
    def SetIdReporte(self, valor: int) -> None:
        self.idReporte = valor;

    def GetCumplioMeta(self) -> bool:
        return self.cumplioMeta;
    def SetCumplioMeta(self, valor: bool) -> None:
        self.cumplioMeta = valor;

    def GetCasosCerrados(self) -> int:
        return self.casosCerrados;
    def SetCasosCerrados(self, valor: int) -> None:
        self.casosCerrados = valor;


# ============================================================
# CLASE CONEXION
# Maneja todas las operaciones con la base de datos
# ============================================================

class Conexion:

    # Cadena de conexión a MySQL via ODBC
    strConnection: str = """
        Driver={MySQL ODBC 9.6 Unicode Driver};
        Server=localhost;
        Database=db_backoffice;
        PORT=3306;
        user=root;
        password=;
        """

    # ----------------------------------------------------------
    # AREAS - SELECT todas
    # ----------------------------------------------------------
    def SelectAreas(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_areas()}");

        listaArea: list = [];          # Lista donde se guardarán todas las áreas
        for fila in cursor:            # Recorre cada fila que devuelve el procedimiento
            area = Areas();            # Crea un objeto área vacío por cada fila
            area.idArea      = fila[0];
            area.nomArea     = fila[1];
            area.descripcion = fila[2];
            area.activa      = fila[3];
            listaArea.append(area);    # Agrega el área a la lista

        cursor.close();
        conexion.close();
        return listaArea;

    # ----------------------------------------------------------
    # AREAS - SELECT por ID
    # ----------------------------------------------------------
    def SelectAreaId(self, idArea: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_area_id(?)}", idArea);

        area = None;                   # Si no encuentra nada, retorna None
        for fila in cursor:
            area = Areas();
            area.idArea      = fila[0];
            area.nomArea     = fila[1];
            area.descripcion = fila[2];
            area.activa      = fila[3];

        cursor.close();
        conexion.close();
        return area;

    # ----------------------------------------------------------
    # AREAS - INSERT
    # ----------------------------------------------------------
    def InsertArea(self, area: Areas) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_area(?, ?, ?)}",
            area.nomArea,      # ? 1
            area.descripcion,  # ? 2
            area.activa        # ? 3
        );
        conexion.commit();     # Confirma los cambios en la BD
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # AREAS - UPDATE
    # ----------------------------------------------------------
    def UpdateArea(self, area: Areas) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_area(?, ?, ?, ?)}",
            area.idArea,       # ? 1 -> id del área a modificar
            area.nomArea,      # ? 2
            area.descripcion,  # ? 3
            area.activa        # ? 4
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # AREAS - DELETE
    # ----------------------------------------------------------
    def DeleteArea(self, idArea: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_area(?)}", idArea);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CARGOS - SELECT todas
    # ----------------------------------------------------------
    def SelectCargos(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_cargos()}");

        listaCargos: list = [];
        for fila in cursor:
            cargo = Cargos();
            cargo.idCargo  = fila[0];
            cargo.nomCargo = fila[1];
            cargo.nivel    = fila[2];
            cargo.activo   = fila[3];
            listaCargos.append(cargo);

        cursor.close();
        conexion.close();
        return listaCargos;

    # ----------------------------------------------------------
    # CARGOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectCargoId(self, idCargo: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_cargo_id(?)}", idCargo);

        cargo = None;
        for fila in cursor:
            cargo = Cargos();
            cargo.idCargo  = fila[0];
            cargo.nomCargo = fila[1];
            cargo.nivel    = fila[2];
            cargo.activo   = fila[3];

        cursor.close();
        conexion.close();
        return cargo;

    # ----------------------------------------------------------
    # CARGOS - INSERT
    # ----------------------------------------------------------
    def InsertCargo(self, cargo: Cargos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_cargo(?, ?, ?)}",
            cargo.nomCargo,
            cargo.nivel,
            cargo.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CARGOS - UPDATE
    # ----------------------------------------------------------
    def UpdateCargo(self, cargo: Cargos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_cargo(?, ?, ?, ?)}",
            cargo.idCargo,
            cargo.nomCargo,
            cargo.nivel,
            cargo.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CARGOS - DELETE
    # ----------------------------------------------------------
    def DeleteCargo(self, idCargo: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_cargo(?)}", idCargo);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ASESORES - SELECT todas
    # ----------------------------------------------------------
    def SelectAsesores(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_asesores()}");

        listaAsesores: list = [];
        for fila in cursor:
            asesor = Asesores();
            asesor.idAsesor     = fila[0];
            asesor.cedula       = fila[1];
            asesor.nombre       = fila[2];
            asesor.email        = fila[3];
            asesor.telefono     = fila[4];
            asesor.idArea       = fila[5];
            asesor.idCargo      = fila[6];
            asesor.fechaIngreso = fila[7];
            asesor.activo       = fila[8];
            listaAsesores.append(asesor);

        cursor.close();
        conexion.close();
        return listaAsesores;

    # ----------------------------------------------------------
    # ASESORES - SELECT por ID
    # ----------------------------------------------------------
    def SelectAsesorId(self, idAsesor: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_asesor_id(?)}", idAsesor);

        asesor = None;
        for fila in cursor:
            asesor = Asesores();
            asesor.idAsesor     = fila[0];
            asesor.cedula       = fila[1];
            asesor.nombre       = fila[2];
            asesor.email        = fila[3];
            asesor.telefono     = fila[4];
            asesor.idArea       = fila[5];
            asesor.idCargo      = fila[6];
            asesor.fechaIngreso = fila[7];
            asesor.activo       = fila[8];

        cursor.close();
        conexion.close();
        return asesor;

    # ----------------------------------------------------------
    # ASESORES - INSERT
    # ----------------------------------------------------------
    def InsertAsesor(self, asesor: Asesores) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_asesor(?, ?, ?, ?, ?, ?, ?, ?)}",
            asesor.cedula,
            asesor.nombre,
            asesor.email,
            asesor.telefono,
            asesor.idArea,
            asesor.idCargo,
            asesor.fechaIngreso,
            asesor.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ASESORES - UPDATE
    # ----------------------------------------------------------
    def UpdateAsesor(self, asesor: Asesores) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_asesor(?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            asesor.idAsesor,
            asesor.cedula,
            asesor.nombre,
            asesor.email,
            asesor.telefono,
            asesor.idArea,
            asesor.idCargo,
            asesor.fechaIngreso,
            asesor.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ASESORES - DELETE
    # ----------------------------------------------------------
    def DeleteAsesor(self, idAsesor: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_asesor(?)}", idAsesor);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # TIPOS CASO - SELECT todas
    # ----------------------------------------------------------
    def SelectTiposCaso(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_tiposCaso()}");

        listaTiposCaso: list = [];
        for fila in cursor:
            tipocaso = TiposCaso();
            tipocaso.idTipoCaso  = fila[0];
            tipocaso.nomTipo     = fila[1];
            tipocaso.descripcion = fila[2];
            tipocaso.tiempoMeta  = fila[3];
            tipocaso.activo      = fila[4];
            listaTiposCaso.append(tipocaso);

        cursor.close();
        conexion.close();
        return listaTiposCaso;

    # ----------------------------------------------------------
    # TIPOS CASO - SELECT por ID
    # ----------------------------------------------------------
    def SelectTiposCasoId(self, idTipoCaso: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_tipoCaso_id(?)}", idTipoCaso);

        tipocaso = None;
        for fila in cursor:
            tipocaso = TiposCaso();
            tipocaso.idTipoCaso  = fila[0];
            tipocaso.nomTipo     = fila[1];
            tipocaso.descripcion = fila[2];
            tipocaso.tiempoMeta  = fila[3];
            tipocaso.activo      = fila[4];

        cursor.close();
        conexion.close();
        return tipocaso;

    # ----------------------------------------------------------
    # TIPOS CASO - INSERT
    # ----------------------------------------------------------
    def InsertTipoCaso(self, tipocaso: TiposCaso) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_tipoCaso(?, ?, ?, ?)}",
            tipocaso.nomTipo,
            tipocaso.descripcion,
            tipocaso.tiempoMeta,
            tipocaso.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # TIPOS CASO - UPDATE
    # ----------------------------------------------------------
    def UpdateTipoCaso(self, tipocaso: TiposCaso) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_tipoCaso(?, ?, ?, ?, ?)}",
            tipocaso.idTipoCaso,
            tipocaso.nomTipo,
            tipocaso.descripcion,
            tipocaso.tiempoMeta,
            tipocaso.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # TIPOS CASO - DELETE
    # ----------------------------------------------------------
    def DeleteTipoCaso(self, idTipoCaso: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_tipoCaso(?)}", idTipoCaso);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # PRIORIDADES - SELECT todas
    # ----------------------------------------------------------
    def SelectPrioridades(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_prioridades()}");

        listaPrioridades: list = [];
        for fila in cursor:
            prioridad = Prioridades();
            prioridad.idPrioridad  = fila[0];
            prioridad.nomPrioridad = fila[1];
            prioridad.nivel        = fila[2];
            prioridad.activa       = fila[3];
            listaPrioridades.append(prioridad);

        cursor.close();
        conexion.close();
        return listaPrioridades;

    # ----------------------------------------------------------
    # PRIORIDADES - SELECT por ID
    # ----------------------------------------------------------
    def SelectPrioridadId(self, idPrioridad: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_prioridad_id(?)}", idPrioridad);

        prioridad = None;
        for fila in cursor:
            prioridad = Prioridades();
            prioridad.idPrioridad  = fila[0];
            prioridad.nomPrioridad = fila[1];
            prioridad.nivel        = fila[2];
            prioridad.activa       = fila[3];

        cursor.close();
        conexion.close();
        return prioridad;

    # ----------------------------------------------------------
    # PRIORIDADES - INSERT
    # ----------------------------------------------------------
    def InsertPrioridad(self, prioridad: Prioridades) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_prioridad(?, ?, ?)}",
            prioridad.nomPrioridad,
            prioridad.nivel,
            prioridad.activa
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # PRIORIDADES - UPDATE
    # ----------------------------------------------------------
    def UpdatePrioridad(self, prioridad: Prioridades) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_prioridad(?, ?, ?, ?)}",
            prioridad.idPrioridad,
            prioridad.nomPrioridad,
            prioridad.nivel,
            prioridad.activa
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # PRIORIDADES - DELETE
    # ----------------------------------------------------------
    def DeletePrioridad(self, idPrioridad: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_prioridad(?)}", idPrioridad);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ESTADOS CASO - SELECT todas
    # ----------------------------------------------------------
    def SelectEstadosCaso(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_estadosCaso()}");

        listaEstadosCaso: list = [];
        for fila in cursor:
            estadocaso = estadosCaso();
            estadocaso.idEstado    = fila[0];
            estadocaso.nomEstado   = fila[1];
            estadocaso.descripcion = fila[2];
            estadocaso.esfinal     = fila[3];
            estadocaso.activo      = fila[4];
            listaEstadosCaso.append(estadocaso);

        cursor.close();
        conexion.close();
        return listaEstadosCaso;

    # ----------------------------------------------------------
    # ESTADOS CASO - SELECT por ID
    # ----------------------------------------------------------
    def SelectEstadoCasoId(self, idEstadoCaso: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_estadoCaso_id(?)}", idEstadoCaso);

        estadocaso = None;
        for fila in cursor:
            estadocaso = estadosCaso();
            estadocaso.idEstado    = fila[0];
            estadocaso.nomEstado   = fila[1];
            estadocaso.descripcion = fila[2];
            estadocaso.esfinal     = fila[3];
            estadocaso.activo      = fila[4];

        cursor.close();
        conexion.close();
        return estadocaso;

    # ----------------------------------------------------------
    # ESTADOS CASO - INSERT
    # ----------------------------------------------------------
    def InsertEstadoCaso(self, estadocaso: estadosCaso) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_estadoCaso(?, ?, ?, ?)}",
            estadocaso.nomEstado,
            estadocaso.descripcion,
            estadocaso.esfinal,
            estadocaso.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ESTADOS CASO - UPDATE
    # ----------------------------------------------------------
    def UpdateEstadoCaso(self, estadocaso: estadosCaso) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_estadoCaso(?, ?, ?, ?, ?)}",
            estadocaso.idEstado,
            estadocaso.nomEstado,
            estadocaso.descripcion,
            estadocaso.esfinal,
            estadocaso.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ESTADOS CASO - DELETE
    # ----------------------------------------------------------
    def DeleteEstadoCaso(self, idEstadoCaso: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_estadoCaso(?)}", idEstadoCaso);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CANALES - SELECT todas
    # ----------------------------------------------------------
    def SelectCanales(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_canales()}");

        listaCanales: list = [];
        for fila in cursor:
            canal = Canales();
            canal.idCanal     = fila[0];
            canal.nomCanal    = fila[1];
            canal.descripcion = fila[2];
            canal.activo      = fila[3];
            listaCanales.append(canal);

        cursor.close();
        conexion.close();
        return listaCanales;

    # ----------------------------------------------------------
    # CANALES - SELECT por ID
    # ----------------------------------------------------------
    def SelectCanalId(self, idCanal: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_canal_id(?)}", idCanal);

        canal = None;
        for fila in cursor:
            canal = Canales();
            canal.idCanal     = fila[0];
            canal.nomCanal    = fila[1];
            canal.descripcion = fila[2];
            canal.activo      = fila[3];

        cursor.close();
        conexion.close();
        return canal;

    # ----------------------------------------------------------
    # CANALES - INSERT
    # ----------------------------------------------------------
    def InsertCanal(self, canal: Canales) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_canal(?, ?, ?)}",
            canal.nomCanal,
            canal.descripcion,
            canal.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CANALES - UPDATE
    # ----------------------------------------------------------
    def UpdateCanal(self, canal: Canales) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_canal(?, ?, ?, ?)}",
            canal.idCanal,
            canal.nomCanal,
            canal.descripcion,
            canal.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CANALES - DELETE
    # ----------------------------------------------------------
    def DeleteCanal(self, idCanal: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_canal(?)}", idCanal);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CLIENTES - SELECT todas
    # ----------------------------------------------------------
    def SelectClientes(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_clientes()}");

        listaClientes: list = [];
        for fila in cursor:
            cliente = Clientes();
            cliente.idCliente     = fila[0];
            cliente.documento     = fila[1];
            cliente.nombre        = fila[2];
            cliente.email         = fila[3];
            cliente.telefono      = fila[4];
            cliente.fechaRegistro = fila[5];
            cliente.activo        = fila[6];
            listaClientes.append(cliente);

        cursor.close();
        conexion.close();
        return listaClientes;

    # ----------------------------------------------------------
    # CLIENTES - SELECT por ID
    # ----------------------------------------------------------
    def SelectClienteId(self, idCliente: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_cliente_id(?)}", idCliente);

        cliente = None;
        for fila in cursor:
            cliente = Clientes();
            cliente.idCliente     = fila[0];
            cliente.documento     = fila[1];
            cliente.nombre        = fila[2];
            cliente.email         = fila[3];
            cliente.telefono      = fila[4];
            cliente.fechaRegistro = fila[5];
            cliente.activo        = fila[6];

        cursor.close();
        conexion.close();
        return cliente;

    # ----------------------------------------------------------
    # CLIENTES - INSERT
    # ----------------------------------------------------------
    def InsertCliente(self, cliente: Clientes) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_cliente(?, ?, ?, ?, ?, ?)}",
            cliente.documento,
            cliente.nombre,
            cliente.email,
            cliente.telefono,
            cliente.fechaRegistro,
            cliente.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CLIENTES - UPDATE
    # ----------------------------------------------------------
    def UpdateCliente(self, cliente: Clientes) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_cliente(?, ?, ?, ?, ?, ?, ?)}",
            cliente.idCliente,
            cliente.documento,
            cliente.nombre,
            cliente.email,
            cliente.telefono,
            cliente.fechaRegistro,
            cliente.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CLIENTES - DELETE
    # ----------------------------------------------------------
    def DeleteCliente(self, idCliente: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_cliente(?)}", idCliente);
        conexion.commit();
        cursor.close();
        conexion.close();

            # ----------------------------------------------------------
    #   CASOS - SELECT todas
    # ----------------------------------------------------------
    def SelectCasos(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_casos()}");

        listaCasos: list = [];
        for fila in cursor:
            caso = Casos();
            caso.idCaso          = fila[0];
            caso.idCliente       = fila[1];
            caso.idTipoCaso      = fila[2];
            caso.idPrioridad     = fila[3];
            caso.idCanal         = fila[4];
            caso.idEstado        = fila[5];
            caso.idAsesor        = fila[6];
            caso.descripcion     = fila[7];
            caso.fechaApertura   = fila[8];
            caso.fechaCierre     = fila[9];
            listaCasos.append(caso);

        cursor.close();
        conexion.close();
        return listaCasos;

    # ----------------------------------------------------------
    # CASOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectCasosId(self, idCaso: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_caso_id(?)}", idCaso);

        caso = None;
        for fila in cursor:
            caso = Casos();
            caso.idCaso          = fila[0];
            caso.idCliente       = fila[1];
            caso.idTipoCaso      = fila[2];
            caso.idPrioridad     = fila[3];
            caso.idCanal         = fila[4];
            caso.idEstado        = fila[5];
            caso.idAsesor        = fila[6];
            caso.descripcion     = fila[7];
            caso.fechaApertura   = fila[8];
            caso.fechaCierre     = fila[9];

        cursor.close();
        conexion.close();
        return caso;

    # ----------------------------------------------------------
    # CASOS - INSERT
    # ----------------------------------------------------------
    def InsertCasos(self, caso: Casos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_caso(?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            caso.idCliente,
            caso.idTipoCaso,
            caso.idPrioridad,
            caso.idCanal,
            caso.idEstado,
            caso.idAsesor,
            caso.descripcion,
            caso.fechaApertura,
            caso.fechaCierre
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CASOS - UPDATE
    # ----------------------------------------------------------
    def UpdateCasos(self, caso: Casos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_caso(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            caso.idCaso,
            caso.idCliente,
            caso.idTipoCaso,
            caso.idPrioridad,
            caso.idCanal,
            caso.idEstado,
            caso.idAsesor,
            caso.descripcion,
            caso.fechaApertura,
            caso.fechaCierre
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # CASOS - DELETE
    # ----------------------------------------------------------
    def DeleteCasos(self, idCaso: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_caso(?)}", idCaso);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    #   SEGUIMIENTOS CASOS - SELECT todas
    # ----------------------------------------------------------
    def SelectSeguimientos(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_seguimientos()}");

        listaSeguimientos: list = [];
        for fila in cursor:
            seguimiento = seguimientoCasos();
            seguimiento.idSeguimiento   = fila[0];
            seguimiento.idCaso          = fila[1];
            seguimiento.idAsesor        = fila[2];
            seguimiento.idEstado        = fila[3];
            seguimiento.nota            = fila[4];
            seguimiento.fecharegistro   = fila[5];
            listaSeguimientos.append(seguimiento);

        cursor.close();
        conexion.close();
        return listaSeguimientos;

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectSeguimientoId(self, idSeguimiento: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_seguimiento_id(?)}", idSeguimiento);

        seguimiento = None;
        for fila in cursor:
            seguimiento = seguimientoCasos();
            seguimiento.idSeguimiento   = fila[0];
            seguimiento.idCaso          = fila[1];
            seguimiento.idAsesor        = fila[2];
            seguimiento.idEstado        = fila[3];
            seguimiento.nota            = fila[4];
            seguimiento.fecharegistro   = fila[5];

        cursor.close();
        conexion.close();
        return seguimiento;

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - INSERT
    # ----------------------------------------------------------
    def InsertSeguimiento(self, seguimiento: seguimientoCasos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_seguimiento(?, ?, ?, ?, ?)}",
            seguimiento.idCaso,
            seguimiento.idAsesor,
            seguimiento.idEstado,
            seguimiento.nota,
            seguimiento.fecharegistro
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # SEGUIMIENTO CASOS - UPDATE
    # ----------------------------------------------------------
    def UpdateSeguimiento(self, seguimiento: seguimientoCasos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_seguimiento(?, ?, ?, ?, ?, ?)}",
            seguimiento.idSeguimiento,
            seguimiento.idCaso,
            seguimiento.idAsesor,
            seguimiento.idEstado,
            seguimiento.nota,
            seguimiento.fecharegistro
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # SEGUIMIENTOS CASOS - DELETE
    # ----------------------------------------------------------
    def DeleteSeguimiento(self, idSeguimiento: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_seguimiento(?)}", idSeguimiento);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    #   TURNOS - SELECT todas
    # ----------------------------------------------------------
    def SelectTurnos(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_turnos()}");

        listaTurnos: list = [];
        for fila in cursor:
            turno = Turnos();
            turno.idTurno      = fila[0];
            turno.nomturno     = fila[1];
            turno.horaInicio   = fila[2];
            turno.horaFin      = fila[3];
            turno.activo       = fila[4];
            listaTurnos.append(turno);

        cursor.close();
        conexion.close();
        return listaTurnos;

    # ----------------------------------------------------------
    # TURNOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectTurnoId(self, idTurno: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_turno_id(?)}", idTurno);

        turno = None;
        for fila in cursor:
            turno = Turnos();
            turno.idTurno      = fila[0];
            turno.nomturno     = fila[1];
            turno.horaInicio   = fila[2];
            turno.horaFin      = fila[3];
            turno.activo       = fila[4];
        cursor.close();
        conexion.close();
        return turno;

    # ----------------------------------------------------------
    # TURNOS - INSERT
    # ----------------------------------------------------------
    def InsertTurno(self, turno: Turnos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_turno(?, ?, ?, ?)}",
            turno.nomturno,
            turno.horaInicio,
            turno.horaFin,
            turno.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # TURNOS - UPDATE
    # ----------------------------------------------------------
    def UpdateTurno(self, turno: Turnos) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_turno(?, ?, ?, ?, ?)}",
            turno.idTurno,
            turno.nomturno,
            turno.horaInicio,
            turno.horaFin,
            turno.activo
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # TURNOS - DELETE
    # ----------------------------------------------------------
    def DeleteTurno(self, idTurno: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_turno(?)}", idTurno);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    #   ASISTENCIAS - SELECT todas
    # ----------------------------------------------------------
    def SelectAsistencias(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_asistencias()}");

        listaAsistencias: list = [];
        for fila in cursor:
            asistencia = Asistencia();
            asistencia.idAsistencia      = fila[0];
            asistencia.idAsesor          = fila[1];
            asistencia.idTurno           = fila[2];
            asistencia.fecha             = fila[3];
            asistencia.horaEntrada       = fila[4];
            asistencia.horaSalida        = fila[5];
            asistencia.minutosTrabajados = fila[6];
            listaAsistencias.append(asistencia);

        cursor.close();
        conexion.close();
        return listaAsistencias;

    # ----------------------------------------------------------
    # ASISTENCIA - SELECT por ID
    # ----------------------------------------------------------
    def SelectAsistenciaId(self, idAsistencia: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_asistencia_id(?)}", idAsistencia);

        asistencia = None;
        for fila in cursor:
            asistencia = Asistencia();
            asistencia.idAsistencia      = fila[0];
            asistencia.idAsesor          = fila[1];
            asistencia.idTurno           = fila[2];
            asistencia.fecha             = fila[3];
            asistencia.horaEntrada       = fila[4];
            asistencia.horaSalida        = fila[5];
            asistencia.minutosTrabajados = fila[6];
        cursor.close();
        conexion.close();
        return asistencia;

    # ----------------------------------------------------------
    # ASISTENCIA - INSERT
    # ----------------------------------------------------------
    def InsertAsitencia(self, asistencia: Asistencia) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_asistencia(?, ?, ?, ?, ?, ?)}",
            asistencia.idAsesor,
            asistencia.idTurno,
            asistencia.fecha,
            asistencia.horaEntrada,
            asistencia.horaSalida,
            asistencia.minutosTrabajados
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ASISTENCIA - UPDATE
    # ----------------------------------------------------------
    def UpdateAsistencia(self, asistencia: Asistencia) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_asistencia(?, ?, ?, ?, ?, ?, ?)}",
            asistencia.idAsistencia,
            asistencia.idAsesor,
            asistencia.idTurno,
            asistencia.fecha,
            asistencia.horaEntrada,
            asistencia.horaSalida,
            asistencia.minutosTrabajados
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # ASISTENCIA - DELETE
    # ----------------------------------------------------------
    def DeleteAsistencia(self, idAsistencia: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_asistencia(?)}", idAsistencia);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    #   METAS PRODUCTIVIDAD - SELECT todas
    # ----------------------------------------------------------
    def SelectMetasProductividad(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_metas()}");

        listaMetas: list = [];
        for fila in cursor:
            meta = MetasProductividad();
            meta.idMeta          = fila[0];
            meta.idArea          = fila[1];
            meta.idTipoCaso      = fila[2];
            meta.casosMetaDia    = fila[3];
            meta.vigenciaDesde   = fila[4];
            meta.vigenciaHasta   = fila[5];
            meta.activa          = fila[6];
            listaMetas.append(meta);

        cursor.close();
        conexion.close();
        return listaMetas;

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - SELECT por ID
    # ----------------------------------------------------------
    def SelectMetaProductividadId(self, idMeta: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_meta_id(?)}", idMeta);

        meta = None;
        for fila in cursor:
            meta = MetasProductividad();
            meta.idMeta          = fila[0];
            meta.idArea          = fila[1];
            meta.idTipoCaso      = fila[2];
            meta.casosMetaDia    = fila[3];
            meta.vigenciaDesde   = fila[4];
            meta.vigenciaHasta   = fila[5];
            meta.activa          = fila[6];
        cursor.close();
        conexion.close();
        return meta;

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - INSERT
    # ----------------------------------------------------------
    def InsertMeta(self, meta: MetasProductividad) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_meta(?, ?, ?, ?, ?, ?)}",
            meta.idArea,
            meta.idTipoCaso,
            meta.casosMetaDia,
            meta.vigenciaDesde,
            meta.vigenciaHasta,
            meta.activa
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - UPDATE
    # ----------------------------------------------------------
    def UpdateMetaProductividad(self, meta: MetasProductividad) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_meta(?, ?, ?, ?, ?, ?, ?)}",
            meta.idMeta,
            meta.idArea,
            meta.idTipoCaso,
            meta.casosMetaDia,
            meta.vigenciaDesde,
            meta.vigenciaHasta,
            meta.activa
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # META PRODUCTIVIDAD - DELETE
    # ----------------------------------------------------------
    def DeleteMetaProductividad(self, idMeta: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_meta(?)}", idMeta);
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    #   EVALUACIONES - SELECT todas
    # ----------------------------------------------------------
    def SelectEvaluaciones(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_evaluaciones()}");

        listaEvaluaciones: list = [];
        for fila in cursor:
            evaluacion = Evaluaciones();
            evaluacion.idEvaluacion      = fila[0];
            evaluacion.idAsesor          = fila[1];
            evaluacion.periodo           = fila[2];
            evaluacion.calidad           = fila[3];
            evaluacion.puntualidad       = fila[4];
            evaluacion.casosGestionados  = fila[5];
            evaluacion.nota              = fila[6];
            evaluacion.fechaEvaluacion   = fila[7];
            listaEvaluaciones.append(evaluacion);

        cursor.close();
        conexion.close();
        return listaEvaluaciones;

    # ----------------------------------------------------------
    # EVALUACIONES - SELECT por ID
    # ----------------------------------------------------------
    def SelectEvaluacionId(self, idEvaluacion: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_evaluacion_id(?)}", idEvaluacion);

        evaluacion = None;
        for fila in cursor:
            evaluacion = Evaluaciones();
            evaluacion.idEvaluacion      = fila[0];
            evaluacion.idAsesor          = fila[1];
            evaluacion.periodo           = fila[2];
            evaluacion.calidad           = fila[3];
            evaluacion.puntualidad       = fila[4];
            evaluacion.casosGestionados  = fila[5];
            evaluacion.nota              = fila[6];
            evaluacion.fechaEvaluacion   = fila[7];
        cursor.close();
        conexion.close();
        return evaluacion;

    # ----------------------------------------------------------
    # EVALUACIONES - INSERT
    # ----------------------------------------------------------
    def InsertEvaluacion(self, evaluacion: Evaluaciones) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_evaluacion(?, ?, ?, ?, ?, ?, ?)}",
            evaluacion.idAsesor,
            evaluacion.periodo,
            evaluacion.calidad,
            evaluacion.puntualidad,
            evaluacion.casosGestionados,
            evaluacion.nota,
            evaluacion.fechaEvaluacion
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # EVALUACIONES - UPDATE
    # ----------------------------------------------------------
    def UpdateEvaluacion(self, evaluacion: Evaluaciones) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_evaluacion(?, ?, ?, ?, ?, ?, ?, ?)}",
            evaluacion.idEvaluacion,
            evaluacion.idAsesor,
            evaluacion.periodo,
            evaluacion.calidad,
            evaluacion.puntualidad,
            evaluacion.casosGestionados,
            evaluacion.nota,
            evaluacion.fechaEvaluacion
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # EVALUACIONES - DELETE
    # ----------------------------------------------------------
    def DeleteEvaluacion(self, idEvaluacion: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_evaluacion(?)}", idEvaluacion);
        conexion.commit();
        cursor.close();
        conexion.close();

   # ----------------------------------------------------------
    #   REPORTES DIARIOS - SELECT todas
    # ----------------------------------------------------------
    def SelectReportesDiarios(self) -> list:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_reportes()}");

        listaReportes: list = [];
        for fila in cursor:
            reporte = ReportesDiarios();
            reporte.idReporte      = fila[0];
            reporte.idAsesor       = fila[1];
            reporte.fecha          = fila[2];
            reporte.casosAbiertos  = fila[3];
            reporte.casosCerrados  = fila[4];
            reporte.casosEnProceso = fila[5];
            reporte.tiempoPromedio = fila[6];
            reporte.cumplioMeta    = fila[7];
            listaReportes.append(reporte);

        cursor.close();
        conexion.close();
        return listaReportes;

    # ----------------------------------------------------------
    # REPORTES DIARIOS - SELECT por ID
    # ----------------------------------------------------------
    def SelectReporteDiarioId(self, idReporte: int):
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_select_reporte_id(?)}", idReporte);

        reporte = None;
        for fila in cursor:
            reporte = ReportesDiarios();
            reporte.idReporte      = fila[0];
            reporte.idAsesor       = fila[1];
            reporte.fecha          = fila[2];
            reporte.casosAbiertos  = fila[3];
            reporte.casosCerrados  = fila[4];
            reporte.casosEnProceso = fila[5];
            reporte.tiempoPromedio = fila[6];
            reporte.cumplioMeta    = fila[7];
        cursor.close();
        conexion.close();
        return reporte;

    # ----------------------------------------------------------
    # REPORTES DIARIOS - INSERT
    # ----------------------------------------------------------
    def InsertReporteDiario(self, reporte: ReportesDiarios) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_insert_reporte(?, ?, ?, ?, ?, ?, ?)}",
            reporte.idAsesor,
            reporte.fecha,
            reporte.casosAbiertos,
            reporte.casosCerrados,
            reporte.casosEnProceso,
            reporte.tiempoPromedio,
            reporte.cumplioMeta
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # REPORTE DIARIOS - UPDATE
    # ----------------------------------------------------------
    def UpdateReporteDiario(self, reporte: ReportesDiarios) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute(
            "{CALL proc_update_reporte(?, ?, ?, ?, ?, ?, ?, ?)}",
            reporte.idReporte,
            reporte.idAsesor,
            reporte.fecha,
            reporte.casosAbiertos,
            reporte.casosCerrados,
            reporte.casosEnProceso,
            reporte.tiempoPromedio,
            reporte.cumplioMeta
        );
        conexion.commit();
        cursor.close();
        conexion.close();

    # ----------------------------------------------------------
    # REPORTE DIARIOS - DELETE
    # ----------------------------------------------------------
    def DeleteReporteDiario(self, idReporte: int) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        cursor.execute("{CALL proc_delete_reporte(?)}", idReporte);
        conexion.commit();
        cursor.close();
        conexion.close();

conexion: Conexion = Conexion();
 
# ============================================================
# TABLA 1: AREAS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: AREAS");
print("="*60);
 
# --- INSERT 5 áreas ---
print("\n-- INSERT 5 áreas --");
areasNuevas = [
    ("Tecnología",    "Soporte técnico y sistemas",           True),
    ("Jurídica",      "Gestión legal y compliance",           True),
    ("Talento Humano","Selección y bienestar del personal",   True),
    ("Auditoría",     "Control interno y revisión de cuentas",True),
    ("Comercial",     "Ventas y atención postventa",          False),
];
for nomArea, descripcion, activa in areasNuevas:
    nueva = Areas();
    nueva.nomArea     = nomArea;
    nueva.descripcion = descripcion;
    nueva.activa      = activa;
    conexion.InsertArea(nueva);
    print("Área insertada: " + nueva.nomArea + ", " + nueva.descripcion + ", " + str(nueva.activa));
 
# --- SELECT todas las áreas ---
print("\n-- SELECT todas las áreas --");
listaArea = conexion.SelectAreas();
for area in listaArea:
    print(str(area.idArea) + ", " + area.nomArea + ", " + area.descripcion + ", " + str(area.activa));
 
# --- SELECT área por ID ---
print("\n-- SELECT área con id=1 --");
area = conexion.SelectAreaId(1);
if area:
    print(str(area.idArea) + ", " + area.nomArea + ", " + area.descripcion + ", " + str(area.activa));
 
# --- UPDATE área con id=1 ---
print("\n-- UPDATE área con id=1 --");
actualizarArea = Areas();
actualizarArea.idArea      = 1;
actualizarArea.nomArea     = "Cartera Actualizada";
actualizarArea.descripcion = "Gestión de cobros, cartera vencida y recuperación";
actualizarArea.activa      = True;
conexion.UpdateArea(actualizarArea);
print("Área actualizada: " + str(actualizarArea.idArea) + ", " + actualizarArea.nomArea + ", " + str(actualizarArea.activa));
 
# --- DELETE área con id=9 ---
print("\n-- DELETE área con id=9 --");
conexion.DeleteArea(9);
print("Área con id=9 eliminada correctamente");
 
 
# ============================================================
# TABLA 2: CARGOS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: CARGOS");
print("="*60);
 
# --- INSERT 5 cargos ---
print("\n-- INSERT 5 cargos --");
cargosNuevos = [
    ("Analista",        1),
    ("Especialista",    2),
    ("Líder de Equipo", 3),
    ("Jefe de Área",    4),
    ("Director",        5),
];
for nomCargo, nivel in cargosNuevos:
    nuevo = Cargos();
    nuevo.nomCargo = nomCargo;
    nuevo.nivel    = nivel;
    nuevo.activo   = True;
    conexion.InsertCargo(nuevo);
    print("Cargo insertado: " + nuevo.nomCargo + ", nivel: " + str(nuevo.nivel));
 
# --- SELECT todos los cargos ---
print("\n-- SELECT todos los cargos --");
listaCargos = conexion.SelectCargos();
for cargo in listaCargos:
    print(str(cargo.idCargo) + ", " + cargo.nomCargo + ", " + str(cargo.nivel) + ", " + str(cargo.activo));
 
# --- SELECT cargo por ID ---
print("\n-- SELECT cargo con id=1 --");
cargo = conexion.SelectCargoId(1);
if cargo:
    print(str(cargo.idCargo) + ", " + cargo.nomCargo + ", " + str(cargo.nivel) + ", " + str(cargo.activo));
 
# --- UPDATE cargo con id=1 ---
print("\n-- UPDATE cargo con id=1 --");
actualizarCargo = Cargos();
actualizarCargo.idCargo  = 1;
actualizarCargo.nomCargo = "Asesor Junior Actualizado";
actualizarCargo.nivel    = 1;
actualizarCargo.activo   = True;
conexion.UpdateCargo(actualizarCargo);
print("Cargo actualizado: " + str(actualizarCargo.idCargo) + ", " + actualizarCargo.nomCargo + ", " + str(actualizarCargo.nivel));
 
# --- DELETE cargo con id=8 ---
print("\n-- DELETE cargo con id=8 --");
conexion.DeleteCargo(8);
print("Cargo con id=8 eliminado correctamente");
 
 
# ============================================================
# TABLA 3: ASESORES
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: ASESORES");
print("="*60);
 
# --- INSERT 5 asesores ---
print("\n-- INSERT 5 asesores --");
asesoresNuevos = [
    ("20111001", "Juan Pérez",    "jperez@bo.com",    "3011110001", 1, 1),
    ("20111002", "Ana Martínez",  "amartinez@bo.com", "3011110002", 2, 2),
    ("20111003", "Luis Herrera",  "lherrera@bo.com",  "3011110003", 3, 1),
    ("20111004", "Sara Ospina",   "sospina@bo.com",   "3011110004", 4, 3),
    ("20111005", "Diego Vargas",  "dvargas@bo.com",   "3011110005", 5, 2),
];
for cedula, nombre, email, telefono, idArea, idCargo in asesoresNuevos:
    nuevo = Asesores();
    nuevo.cedula       = cedula;
    nuevo.nombre       = nombre;
    nuevo.email        = email;
    nuevo.telefono     = telefono;
    nuevo.idArea       = idArea;
    nuevo.idCargo      = idCargo;
    nuevo.fechaIngreso = datetime.datetime.now();
    nuevo.activo       = True;
    conexion.InsertAsesor(nuevo);
    print("Asesor insertado: " + nuevo.cedula + ", " + nuevo.nombre + ", " + nuevo.email);
 
# --- SELECT todos los asesores ---
print("\n-- SELECT todos los asesores --");
listaAsesores = conexion.SelectAsesores();
for asesor in listaAsesores:
    print(str(asesor.idAsesor) + ", " + asesor.cedula + ", " + asesor.nombre + ", " +
          asesor.email + ", " + asesor.telefono + ", " +
          str(asesor.idArea) + ", " + str(asesor.idCargo) + ", " + str(asesor.activo));
 
# --- SELECT asesor por ID ---
print("\n-- SELECT asesor con id=1 --");
asesor = conexion.SelectAsesorId(1);
if asesor:
    print(str(asesor.idAsesor) + ", " + asesor.cedula + ", " + asesor.nombre + ", " + str(asesor.activo));
 
# --- UPDATE asesor con id=1 ---
print("\n-- UPDATE asesor con id=1 --");
actualizarAsesor = Asesores();
actualizarAsesor.idAsesor     = 1;
actualizarAsesor.cedula       = "10425601";
actualizarAsesor.nombre       = "Laura Gómez Actualizada";
actualizarAsesor.email        = "lgomez2@backoffice.com";
actualizarAsesor.telefono     = "3001234599";
actualizarAsesor.idArea       = 1;
actualizarAsesor.idCargo      = 2;
actualizarAsesor.fechaIngreso = datetime.datetime.now();
actualizarAsesor.activo       = True;
conexion.UpdateAsesor(actualizarAsesor);
print("Asesor actualizado: " + str(actualizarAsesor.idAsesor) + ", " + actualizarAsesor.nombre);
 
# --- DELETE asesor con id=8 ---
print("\n-- DELETE asesor con id=8 --");
conexion.DeleteAsesor(8);
print("Asesor con id=8 eliminado correctamente");
 
 
# ============================================================
# TABLA 4: TIPOS CASO
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: TIPOS CASO");
print("="*60);
 
# --- INSERT 5 tipos de caso ---
print("\n-- INSERT 5 tipos de caso --");
tiposNuevos = [
    ("Queja",            "Inconformidad general del cliente",           45),
    ("Reembolso",        "Devolución de dinero por error en cobro",    120),
    ("Asesoría",         "Consulta o acompañamiento al cliente",        30),
    ("Incidente Técnico","Fallo en plataforma o sistema del cliente",   90),
    ("Cancelación",      "Solicitud de cancelación de producto",       150),
];
for nomTipo, descripcion, tiempoMeta in tiposNuevos:
    nuevo = TiposCaso();
    nuevo.nomTipo     = nomTipo;
    nuevo.descripcion = descripcion;
    nuevo.tiempoMeta  = tiempoMeta;
    nuevo.activo      = True;
    conexion.InsertTipoCaso(nuevo);
    print("Tipo caso insertado: " + nuevo.nomTipo + ", meta: " + str(nuevo.tiempoMeta) + " min");
 
# --- SELECT todos los tipos de caso ---
print("\n-- SELECT todos los tipos de caso --");
listaTiposCaso = conexion.SelectTiposCaso();
for tipocaso in listaTiposCaso:
    print(str(tipocaso.idTipoCaso) + ", " + tipocaso.nomTipo + ", " +
          tipocaso.descripcion + ", " + str(tipocaso.tiempoMeta) + ", " + str(tipocaso.activo));
 
# --- SELECT tipo caso por ID ---
print("\n-- SELECT tipo caso con id=1 --");
tipocaso = conexion.SelectTiposCasoId(1);
if tipocaso:
    print(str(tipocaso.idTipoCaso) + ", " + tipocaso.nomTipo + ", " + str(tipocaso.tiempoMeta));
 
# --- UPDATE tipo caso con id=1 ---
print("\n-- UPDATE tipo caso con id=1 --");
actualizarTipo = TiposCaso();
actualizarTipo.idTipoCaso  = 1;
actualizarTipo.nomTipo     = "Reclamo Factura Actualizado";
actualizarTipo.descripcion = "Inconformidad con el valor facturado - revisado";
actualizarTipo.tiempoMeta  = 100;
actualizarTipo.activo      = True;
conexion.UpdateTipoCaso(actualizarTipo);
print("Tipo caso actualizado: " + str(actualizarTipo.idTipoCaso) + ", " + actualizarTipo.nomTipo);
 
# --- DELETE tipo caso con id=11 ---
print("\n-- DELETE tipo caso con id=11 --");
conexion.DeleteTipoCaso(11);
print("Tipo caso con id=11 eliminado correctamente");
 
 
# ============================================================
# TABLA 5: PRIORIDADES
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: PRIORIDADES");
print("="*60);
 
# --- INSERT 5 prioridades ---
print("\n-- INSERT 5 prioridades --");
prioridadesNuevas = [
    ("Muy Baja",    0),
    ("Programada",  1),
    ("Normal",      2),
    ("Urgente",     3),
    ("Inmediata",   5),
];
for nomPrioridad, nivel in prioridadesNuevas:
    nueva = Prioridades();
    nueva.nomPrioridad = nomPrioridad;
    nueva.nivel        = nivel;
    nueva.activa       = True;
    conexion.InsertPrioridad(nueva);
    print("Prioridad insertada: " + nueva.nomPrioridad + ", nivel: " + str(nueva.nivel));
 
# --- SELECT todas las prioridades ---
print("\n-- SELECT todas las prioridades --");
listaPrioridades = conexion.SelectPrioridades();
for prioridad in listaPrioridades:
    print(str(prioridad.idPrioridad) + ", " + prioridad.nomPrioridad + ", " +
          str(prioridad.nivel) + ", " + str(prioridad.activa));
 
# --- SELECT prioridad por ID ---
print("\n-- SELECT prioridad con id=1 --");
prioridad = conexion.SelectPrioridadId(1);
if prioridad:
    print(str(prioridad.idPrioridad) + ", " + prioridad.nomPrioridad + ", " + str(prioridad.nivel));
 
# --- UPDATE prioridad con id=1 ---
print("\n-- UPDATE prioridad con id=1 --");
actualizarPrioridad = Prioridades();
actualizarPrioridad.idPrioridad  = 1;
actualizarPrioridad.nomPrioridad = "Baja Actualizada";
actualizarPrioridad.nivel        = 1;
actualizarPrioridad.activa       = True;
conexion.UpdatePrioridad(actualizarPrioridad);
print("Prioridad actualizada: " + str(actualizarPrioridad.idPrioridad) + ", " + actualizarPrioridad.nomPrioridad);
 
# --- DELETE prioridad con id=8 ---
print("\n-- DELETE prioridad con id=8 --");
conexion.DeletePrioridad(8);
print("Prioridad con id=8 eliminada correctamente");
 
 
# ============================================================
# TABLA 6: ESTADOS CASO
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: ESTADOS CASO");
print("="*60);
 
# --- INSERT 5 estados de caso ---
print("\n-- INSERT 5 estados de caso --");
estadosNuevos = [
    ("Pendiente Revisión", "Caso asignado pero sin iniciar revisión", False),
    ("En Validación",      "Verificando información del cliente",     False),
    ("Escalado",           "Caso enviado a nivel superior",           False),
    ("Rechazado",          "Caso no procede según políticas",         True ),
    ("Reabierto",          "Caso cerrado que fue vuelto a abrir",     False),
];
for nomEstado, descripcion, esFinal in estadosNuevos:
    nuevo = estadosCaso();
    nuevo.nomEstado   = nomEstado;
    nuevo.descripcion = descripcion;
    nuevo.esfinal     = esFinal;
    nuevo.activo      = True;
    conexion.InsertEstadoCaso(nuevo);
    print("Estado insertado: " + nuevo.nomEstado + ", esFinal: " + str(nuevo.esfinal));
 
# --- SELECT todos los estados ---
print("\n-- SELECT todos los estados de caso --");
listaEstadosCaso = conexion.SelectEstadosCaso();
for estado in listaEstadosCaso:
    print(str(estado.idEstado) + ", " + estado.nomEstado + ", " +
          estado.descripcion + ", " + str(estado.esfinal) + ", " + str(estado.activo));
 
# --- SELECT estado por ID ---
print("\n-- SELECT estado con id=1 --");
estado = conexion.SelectEstadoCasoId(1);
if estado:
    print(str(estado.idEstado) + ", " + estado.nomEstado + ", " + str(estado.esfinal));
 
# --- UPDATE estado con id=1 ---
print("\n-- UPDATE estado con id=1 --");
actualizarEstado = estadosCaso();
actualizarEstado.idEstado    = 1;
actualizarEstado.nomEstado   = "Abierto Actualizado";
actualizarEstado.descripcion = "Caso recién creado y verificado";
actualizarEstado.esfinal     = False;
actualizarEstado.activo      = True;
conexion.UpdateEstadoCaso(actualizarEstado);
print("Estado actualizado: " + str(actualizarEstado.idEstado) + ", " + actualizarEstado.nomEstado);
 
# --- DELETE estado con id=9 ---
print("\n-- DELETE estado con id=9 --");
conexion.DeleteEstadoCaso(9);
print("Estado con id=9 eliminado correctamente");
 
 
# ============================================================
# TABLA 7: CANALES
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: CANALES");
print("="*60);
 
# --- INSERT 5 canales ---
print("\n-- INSERT 5 canales --");
canalesNuevos = [
    ("WhatsApp",    "Casos recibidos por mensajería WhatsApp Business"),
    ("Redes Sociales","Casos recibidos por Facebook o Instagram"),
    ("Presencial",  "Casos atendidos en punto físico"),
    ("App Móvil",   "Casos generados desde la aplicación móvil"),
    ("SMS",         "Casos notificados por mensaje de texto"),
];
for nomCanal, descripcion in canalesNuevos:
    nuevo = Canales();
    nuevo.nomCanal    = nomCanal;
    nuevo.descripcion = descripcion;
    nuevo.activo      = True;
    conexion.InsertCanal(nuevo);
    print("Canal insertado: " + nuevo.nomCanal + ", " + nuevo.descripcion);
 
# --- SELECT todos los canales ---
print("\n-- SELECT todos los canales --");
listaCanales = conexion.SelectCanales();
for canal in listaCanales:
    print(str(canal.idCanal) + ", " + canal.nomCanal + ", " + canal.descripcion + ", " + str(canal.activo));
 
# --- SELECT canal por ID ---
print("\n-- SELECT canal con id=1 --");
canal = conexion.SelectCanalId(1);
if canal:
    print(str(canal.idCanal) + ", " + canal.nomCanal + ", " + str(canal.activo));
 
# --- UPDATE canal con id=1 ---
print("\n-- UPDATE canal con id=1 --");
actualizarCanal = Canales();
actualizarCanal.idCanal     = 1;
actualizarCanal.nomCanal    = "Email Corporativo";
actualizarCanal.descripcion = "Casos recibidos por correo corporativo oficial";
actualizarCanal.activo      = True;
conexion.UpdateCanal(actualizarCanal);
print("Canal actualizado: " + str(actualizarCanal.idCanal) + ", " + actualizarCanal.nomCanal);
 
# --- DELETE canal con id=8 ---
print("\n-- DELETE canal con id=8 --");
conexion.DeleteCanal(8);
print("Canal con id=8 eliminado correctamente");
 
 
# ============================================================
# TABLA 8: CLIENTES
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: CLIENTES");
print("="*60);
 
# --- INSERT 5 clientes ---
print("\n-- INSERT 5 clientes --");
clientesNuevos = [
    ("9001", "Roberto Suárez",  "rsuarez@email.com",  "3200001001"),
    ("9002", "Mónica Ríos",     "mrios@email.com",    "3200001002"),
    ("9003", "Felipe Torres",   "ftorres@email.com",  "3200001003"),
    ("9004", "Claudia Nieto",   "cnieto@email.com",   "3200001004"),
    ("9005", "Samuel Reyes",    "sreyes@email.com",   "3200001005"),
];
for documento, nombre, email, telefono in clientesNuevos:
    nuevo = Clientes();
    nuevo.documento     = documento;
    nuevo.nombre        = nombre;
    nuevo.email         = email;
    nuevo.telefono      = telefono;
    nuevo.fechaRegistro = datetime.datetime.now();
    nuevo.activo        = True;
    conexion.InsertCliente(nuevo);
    print("Cliente insertado: " + nuevo.documento + ", " + nuevo.nombre + ", " + nuevo.email);
 
# --- SELECT todos los clientes ---
print("\n-- SELECT todos los clientes --");
listaClientes = conexion.SelectClientes();
for cliente in listaClientes:
    print(str(cliente.idCliente) + ", " + cliente.documento + ", " + cliente.nombre + ", " +
          cliente.email + ", " + cliente.telefono + ", " + str(cliente.activo));
 
# --- SELECT cliente por ID ---
print("\n-- SELECT cliente con id=1 --");
cliente = conexion.SelectClienteId(1);
if cliente:
    print(str(cliente.idCliente) + ", " + cliente.documento + ", " + cliente.nombre + ", " + str(cliente.activo));
 
# --- UPDATE cliente con id=1 ---
print("\n-- UPDATE cliente con id=1 --");
actualizarCliente = Clientes();
actualizarCliente.idCliente     = 1;
actualizarCliente.documento     = "8001";
actualizarCliente.nombre        = "Pedro Álvarez Actualizado";
actualizarCliente.email         = "palvarez2@email.com";
actualizarCliente.telefono      = "3109001099";
actualizarCliente.fechaRegistro = datetime.datetime.now();
actualizarCliente.activo        = True;
conexion.UpdateCliente(actualizarCliente);
print("Cliente actualizado: " + str(actualizarCliente.idCliente) + ", " + actualizarCliente.nombre);
 
# --- DELETE cliente con id=7 ---
print("\n-- DELETE cliente con id=7 --");
conexion.DeleteCliente(7);
print("Cliente con id=7 eliminado correctamente");
 
 
# ============================================================
# TABLA 9: CASOS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: CASOS");
print("="*60);
 
# --- INSERT 5 casos ---
# Nota: idCliente, idTipoCaso, idPrioridad, idCanal, idEstado, idAsesor deben existir en BD
print("\n-- INSERT 5 casos --");
casosNuevos = [
    (1, 1, 2, 1, 1, 1, "Cliente reporta cobro duplicado en extracto de enero"),
    (2, 3, 1, 3, 2, 2, "Actualización de datos personales y dirección"),
    (3, 4, 4, 2, 2, 3, "Cuenta bloqueada por actividad inusual detectada"),
    (1, 2, 3, 1, 1, 4, "Solicitud de devolución por pago en exceso"),
    (2, 5, 2, 4, 1, 1, "Ajuste de saldo por error en liquidación de producto"),
];
for idCliente, idTipoCaso, idPrioridad, idCanal, idEstado, idAsesor, descripcion in casosNuevos:
    nuevo = Casos();
    nuevo.idCliente    = idCliente;
    nuevo.idTipoCaso   = idTipoCaso;
    nuevo.idPrioridad  = idPrioridad;
    nuevo.idCanal      = idCanal;
    nuevo.idEstado     = idEstado;
    nuevo.idAsesor     = idAsesor;
    nuevo.descripcion  = descripcion;
    nuevo.fechaApertura = datetime.datetime.now();
    nuevo.fechaCierre  = None;
    conexion.InsertCasos(nuevo);
    print("Caso insertado: cliente " + str(nuevo.idCliente) + ", asesor " + str(nuevo.idAsesor) + ", " + nuevo.descripcion[:40] + "...");
 
# --- SELECT todos los casos ---
print("\n-- SELECT todos los casos --");
listaCasos = conexion.SelectCasos();
for caso in listaCasos:
    print(str(caso.idCaso) + ", cli:" + str(caso.idCliente) + ", tip:" + str(caso.idTipoCaso) +
          ", pri:" + str(caso.idPrioridad) + ", est:" + str(caso.idEstado) +
          ", ase:" + str(caso.idAsesor) + ", " + caso.descripcion[:30] + "...");
 
# --- SELECT caso por ID ---
print("\n-- SELECT caso con id=1 --");
caso = conexion.SelectCasosId(1);
if caso:
    print(str(caso.idCaso) + ", " + caso.descripcion + ", " + str(caso.fechaApertura));
 
# --- UPDATE caso con id=1 ---
print("\n-- UPDATE caso con id=1 --");
actualizarCaso = Casos();
actualizarCaso.idCaso       = 1;
actualizarCaso.idCliente    = 1;
actualizarCaso.idTipoCaso   = 1;
actualizarCaso.idPrioridad  = 3;
actualizarCaso.idCanal      = 1;
actualizarCaso.idEstado     = 2;
actualizarCaso.idAsesor     = 1;
actualizarCaso.descripcion  = "Cliente reclama cobro doble - EN PROCESO DE REVISIÓN";
actualizarCaso.fechaApertura = datetime.datetime.now();
actualizarCaso.fechaCierre  = None;
conexion.UpdateCasos(actualizarCaso);
print("Caso actualizado: id=" + str(actualizarCaso.idCaso) + ", estado=" + str(actualizarCaso.idEstado));
 
# --- DELETE caso con id=7 ---
print("\n-- DELETE caso con id=7 --");
conexion.DeleteCasos(7);
print("Caso con id=7 eliminado correctamente");
 
 
# ============================================================
# TABLA 10: SEGUIMIENTOS CASO
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: SEGUIMIENTOS CASO");
print("="*60);
 
# --- INSERT 5 seguimientos ---
print("\n-- INSERT 5 seguimientos --");
seguimientosNuevos = [
    (1, 1, 2, "Caso revisado, se solicita extracto al cliente"),
    (1, 2, 3, "Extracto recibido, en validación con el área de facturación"),
    (2, 2, 1, "Datos actualizados en sistema exitosamente"),
    (3, 3, 4, "Cuenta desbloqueada previa validación de identidad"),
    (4, 1, 2, "Devolución aprobada, pendiente procesamiento en tesorería"),
];
for idCaso, idAsesor, idEstado, nota in seguimientosNuevos:
    nuevo = seguimientoCasos();
    nuevo.idCaso        = idCaso;
    nuevo.idAsesor      = idAsesor;
    nuevo.idEstado      = idEstado;
    nuevo.nota          = nota;
    nuevo.fecharegistro = datetime.datetime.now();
    conexion.InsertSeguimiento(nuevo);
    print("Seguimiento insertado: caso " + str(nuevo.idCaso) + ", asesor " + str(nuevo.idAsesor) + ", " + nuevo.nota[:40] + "...");
 
# --- SELECT todos los seguimientos ---
print("\n-- SELECT todos los seguimientos --");
listaSeguimientos = conexion.SelectSeguimientos();
for seg in listaSeguimientos:
    print(str(seg.idSeguimiento) + ", caso:" + str(seg.idCaso) + ", asesor:" + str(seg.idAsesor) +
          ", estado:" + str(seg.idEstado) + ", " + seg.nota[:35] + "...");
 
# --- SELECT seguimiento por ID ---
print("\n-- SELECT seguimiento con id=1 --");
seg = conexion.SelectSeguimientoId(1);
if seg:
    print(str(seg.idSeguimiento) + ", " + seg.nota + ", " + str(seg.fecharegistro));
 
# --- UPDATE seguimiento con id=1 ---
print("\n-- UPDATE seguimiento con id=1 --");
actualizarSeg = seguimientoCasos();
actualizarSeg.idSeguimiento = 1;
actualizarSeg.idCaso        = 1;
actualizarSeg.idAsesor      = 1;
actualizarSeg.idEstado      = 3;
actualizarSeg.nota          = "Caso revisado y escalado a coordinación para aprobación";
actualizarSeg.fecharegistro = datetime.datetime.now();
conexion.UpdateSeguimiento(actualizarSeg);
print("Seguimiento actualizado: id=" + str(actualizarSeg.idSeguimiento) + ", " + actualizarSeg.nota[:40] + "...");
 
# --- DELETE seguimiento con id=5 ---
print("\n-- DELETE seguimiento con id=5 --");
conexion.DeleteSeguimiento(5);
print("Seguimiento con id=5 eliminado correctamente");
 
 
# ============================================================
# TABLA 11: TURNOS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: TURNOS");
print("="*60);
 
# --- INSERT 5 turnos ---
print("\n-- INSERT 5 turnos --");
turnosNuevos = [
    ("Madrugada",  "00:00:00", "08:00:00"),
    ("Nocturno",   "22:00:00", "06:00:00"),
    ("Extendido",  "06:00:00", "20:00:00"),
    ("Medio Día",  "10:00:00", "18:00:00"),
    ("Rotativo",   "08:00:00", "16:00:00"),
];
for nomturno, horaInicio, horaFin in turnosNuevos:
    nuevo = Turnos();
    nuevo.nomturno   = nomturno;
    nuevo.horaInicio = horaInicio;
    nuevo.horaFin    = horaFin;
    nuevo.activo     = True;
    conexion.InsertTurno(nuevo);
    print("Turno insertado: " + nuevo.nomturno + ", " + str(nuevo.horaInicio) + " - " + str(nuevo.horaFin));
 
# --- SELECT todos los turnos ---
print("\n-- SELECT todos los turnos --");
listaTurnos = conexion.SelectTurnos();
for turno in listaTurnos:
    print(str(turno.idTurno) + ", " + turno.nomturno + ", " +
          str(turno.horaInicio) + ", " + str(turno.horaFin) + ", " + str(turno.activo));
 
# --- SELECT turno por ID ---
print("\n-- SELECT turno con id=1 --");
turno = conexion.SelectTurnoId(1);
if turno:
    print(str(turno.idTurno) + ", " + turno.nomturno + ", " + str(turno.horaInicio));
 
# --- UPDATE turno con id=1 ---
print("\n-- UPDATE turno con id=1 --");
actualizarTurno = Turnos();
actualizarTurno.idTurno    = 1;
actualizarTurno.nomturno   = "Mañana Actualizado";
actualizarTurno.horaInicio = "06:30:00";
actualizarTurno.horaFin    = "14:30:00";
actualizarTurno.activo     = True;
conexion.UpdateTurno(actualizarTurno);
print("Turno actualizado: " + str(actualizarTurno.idTurno) + ", " + actualizarTurno.nomturno);
 
# --- DELETE turno con id=7 ---
print("\n-- DELETE turno con id=7 --");
conexion.DeleteTurno(7);
print("Turno con id=7 eliminado correctamente");
 
 
# ============================================================
# TABLA 12: ASISTENCIAS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: ASISTENCIAS");
print("="*60);
 
# --- INSERT 5 asistencias ---
print("\n-- INSERT 5 asistencias --");
asistenciasNuevas = [
    (1, 1, 480),
    (2, 2, 450),
    (3, 1, 480),
    (4, 3, 360),
    (1, 2, 420),
];
for idAsesor, idTurno, minutos in asistenciasNuevas:
    nueva = Asistencia();
    nueva.idAsesor          = idAsesor;
    nueva.idTurno           = idTurno;
    nueva.fecha             = datetime.datetime.now();
    nueva.horaEntrada       = datetime.datetime.now();
    nueva.horaSalida        = datetime.datetime.now();
    nueva.minutosTrabajados = minutos;
    conexion.InsertAsitencia(nueva);
    print("Asistencia insertada: asesor " + str(nueva.idAsesor) + ", turno " + str(nueva.idTurno) + ", " + str(nueva.minutosTrabajados) + " min");
 
# --- SELECT todas las asistencias ---
print("\n-- SELECT todas las asistencias --");
listaAsistencias = conexion.SelectAsistencias();
for asistencia in listaAsistencias:
    print(str(asistencia.idAsistencia) + ", asesor:" + str(asistencia.idAsesor) +
          ", turno:" + str(asistencia.idTurno) + ", " + str(asistencia.fecha) +
          ", mins:" + str(asistencia.minutosTrabajados));
 
# --- SELECT asistencia por ID ---
print("\n-- SELECT asistencia con id=1 --");
asistencia = conexion.SelectAsistenciaId(1);
if asistencia:
    print(str(asistencia.idAsistencia) + ", asesor:" + str(asistencia.idAsesor) + ", mins:" + str(asistencia.minutosTrabajados));
 
# --- UPDATE asistencia con id=1 ---
print("\n-- UPDATE asistencia con id=1 --");
actualizarAsistencia = Asistencia();
actualizarAsistencia.idAsistencia      = 1;
actualizarAsistencia.idAsesor          = 1;
actualizarAsistencia.idTurno           = 1;
actualizarAsistencia.fecha             = datetime.datetime.now();
actualizarAsistencia.horaEntrada       = datetime.datetime.now();
actualizarAsistencia.horaSalida        = datetime.datetime.now();
actualizarAsistencia.minutosTrabajados = 500;
conexion.UpdateAsistencia(actualizarAsistencia);
print("Asistencia actualizada: id=" + str(actualizarAsistencia.idAsistencia) + ", mins=" + str(actualizarAsistencia.minutosTrabajados));
 
# --- DELETE asistencia con id=5 ---
print("\n-- DELETE asistencia con id=5 --");
conexion.DeleteAsistencia(5);
print("Asistencia con id=5 eliminada correctamente");
 
 
# ============================================================
# TABLA 13: METAS PRODUCTIVIDAD
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: METAS PRODUCTIVIDAD");
print("="*60);
 
# --- INSERT 5 metas ---
print("\n-- INSERT 5 metas de productividad --");
metasNuevas = [
    (1, 1, 15, "2025-01-01", "2025-06-30"),
    (2, 2, 10, "2025-01-01", "2025-12-31"),
    (3, 3, 20, "2025-03-01", "2025-09-30"),
    (4, 4, 8,  "2025-01-01", "2025-12-31"),
    (5, 5, 12, "2025-06-01", "2025-12-31"),
];
for idArea, idTipoCaso, casosMetaDia, vigDesde, vigHasta in metasNuevas:
    nueva = MetasProductividad();
    nueva.idArea        = idArea;
    nueva.idTipoCaso    = idTipoCaso;
    nueva.casosMetaDia  = casosMetaDia;
    nueva.vigenciaDesde = vigDesde;
    nueva.vigenciaHasta = vigHasta;
    nueva.activa        = True;
    conexion.InsertMeta(nueva);
    print("Meta insertada: área " + str(nueva.idArea) + ", tipoCaso " + str(nueva.idTipoCaso) + ", meta/día: " + str(nueva.casosMetaDia));
 
# --- SELECT todas las metas ---
print("\n-- SELECT todas las metas de productividad --");
listaMetas = conexion.SelectMetasProductividad();
for meta in listaMetas:
    print(str(meta.idMeta) + ", área:" + str(meta.idArea) + ", tipoCaso:" + str(meta.idTipoCaso) +
          ", metaDía:" + str(meta.casosMetaDia) + ", desde:" + str(meta.vigenciaDesde) +
          ", hasta:" + str(meta.vigenciaHasta) + ", activa:" + str(meta.activa));
 
# --- SELECT meta por ID ---
print("\n-- SELECT meta con id=1 --");
meta = conexion.SelectMetaProductividadId(1);
if meta:
    print(str(meta.idMeta) + ", área:" + str(meta.idArea) + ", meta/día:" + str(meta.casosMetaDia) + ", activa:" + str(meta.activa));
 
# --- UPDATE meta con id=1 ---
print("\n-- UPDATE meta con id=1 --");
actualizarMeta = MetasProductividad();
actualizarMeta.idMeta        = 1;
actualizarMeta.idArea        = 1;
actualizarMeta.idTipoCaso    = 1;
actualizarMeta.casosMetaDia  = 18;
actualizarMeta.vigenciaDesde = "2025-01-01";
actualizarMeta.vigenciaHasta = "2025-12-31";
actualizarMeta.activa        = True;
conexion.UpdateMetaProductividad(actualizarMeta);
print("Meta actualizada: id=" + str(actualizarMeta.idMeta) + ", nueva meta/día=" + str(actualizarMeta.casosMetaDia));
 
# --- DELETE meta con id=5 ---
print("\n-- DELETE meta con id=5 --");
conexion.DeleteMetaProductividad(5);
print("Meta con id=5 eliminada correctamente");
 
 
# ============================================================
# TABLA 14: EVALUACIONES
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: EVALUACIONES");
print("="*60);
 
# --- INSERT 5 evaluaciones ---
print("\n-- INSERT 5 evaluaciones --");
evaluacionesNuevas = [
    (1, "2025-01", 90.0, 95.0, 120, 92.0),
    (2, "2025-01", 85.0, 88.0,  98, 86.5),
    (3, "2025-01", 78.0, 80.0, 110, 79.0),
    (4, "2025-01", 95.0, 97.0, 135, 96.0),
    (1, "2025-02", 88.0, 91.0, 125, 89.5),
];
for idAsesor, periodo, calidad, puntualidad, casosGestionados, nota in evaluacionesNuevas:
    nueva = Evaluaciones();
    nueva.idAsesor         = idAsesor;
    nueva.periodo          = periodo;
    nueva.calidad          = calidad;
    nueva.puntualidad      = puntualidad;
    nueva.casosGestionados = casosGestionados;
    nueva.nota             = nota;
    nueva.fechaEvaluacion  = datetime.datetime.now();
    conexion.InsertEvaluacion(nueva);
    print("Evaluación insertada: asesor " + str(nueva.idAsesor) + ", periodo " + nueva.periodo + ", nota: " + str(nueva.nota));
 
# --- SELECT todas las evaluaciones ---
print("\n-- SELECT todas las evaluaciones --");
listaEvaluaciones = conexion.SelectEvaluaciones();
for evaluacion in listaEvaluaciones:
    print(str(evaluacion.idEvaluacion) + ", asesor:" + str(evaluacion.idAsesor) +
          ", periodo:" + evaluacion.periodo + ", calidad:" + str(evaluacion.calidad) +
          ", puntualidad:" + str(evaluacion.puntualidad) +
          ", casos:" + str(evaluacion.casosGestionados) + ", nota:" + str(evaluacion.nota));
 
# --- SELECT evaluación por ID ---
print("\n-- SELECT evaluación con id=1 --");
evaluacion = conexion.SelectEvaluacionId(1);
if evaluacion:
    print(str(evaluacion.idEvaluacion) + ", asesor:" + str(evaluacion.idAsesor) + ", nota:" + str(evaluacion.nota));
 
# --- UPDATE evaluación con id=1 ---
print("\n-- UPDATE evaluación con id=1 --");
actualizarEval = Evaluaciones();
actualizarEval.idEvaluacion     = 1;
actualizarEval.idAsesor         = 1;
actualizarEval.periodo          = "2025-01";
actualizarEval.calidad          = 93.0;
actualizarEval.puntualidad      = 96.0;
actualizarEval.casosGestionados = 130;
actualizarEval.nota             = 94.5;
actualizarEval.fechaEvaluacion  = datetime.datetime.now();
conexion.UpdateEvaluacion(actualizarEval);
print("Evaluación actualizada: id=" + str(actualizarEval.idEvaluacion) + ", nueva nota=" + str(actualizarEval.nota));
 
# --- DELETE evaluación con id=5 ---
print("\n-- DELETE evaluación con id=5 --");
conexion.DeleteEvaluacion(5);
print("Evaluación con id=5 eliminada correctamente");
 
 
# ============================================================
# TABLA 15: REPORTES DIARIOS
# ============================================================
 
print("\n" + "="*60);
print("PRUEBAS TABLA: REPORTES DIARIOS");
print("="*60);
 
# --- INSERT 5 reportes ---
print("\n-- INSERT 5 reportes diarios --");
reportesNuevos = [
    (1, "2025-04-01", 5,  12, 3,  35.5, True ),
    (2, "2025-04-01", 3,  8,  4,  42.0, False),
    (3, "2025-04-01", 6,  14, 2,  28.0, True ),
    (4, "2025-04-01", 4,  10, 5,  38.5, True ),
    (1, "2025-04-02", 7,  11, 4,  33.0, False),
];
for idAsesor, fecha, abiertos, cerrados, enProceso, tiempoPromedio, cumplioMeta in reportesNuevos:
    nuevo = ReportesDiarios();
    nuevo.idAsesor       = idAsesor;
    nuevo.fecha          = fecha;
    nuevo.casosAbiertos  = abiertos;
    nuevo.casosCerrados  = cerrados;
    nuevo.casosEnProceso = enProceso;
    nuevo.tiempoPromedio = tiempoPromedio;
    nuevo.cumplioMeta    = cumplioMeta;
    conexion.InsertReporteDiario(nuevo);
    print("Reporte insertado: asesor " + str(nuevo.idAsesor) + ", fecha " + str(nuevo.fecha) +
          ", cerrados:" + str(nuevo.casosCerrados) + ", cumplioMeta:" + str(nuevo.cumplioMeta));
 
# --- SELECT todos los reportes ---
print("\n-- SELECT todos los reportes diarios --");
listaReportes = conexion.SelectReportesDiarios();
for reporte in listaReportes:
    print(str(reporte.idReporte) + ", asesor:" + str(reporte.idAsesor) +
          ", fecha:" + str(reporte.fecha) +
          ", abiertos:" + str(reporte.casosAbiertos) +
          ", cerrados:" + str(reporte.casosCerrados) +
          ", enProceso:" + str(reporte.casosEnProceso) +
          ", tPromedio:" + str(reporte.tiempoPromedio) +
          ", meta:" + str(reporte.cumplioMeta));
 
# --- SELECT reporte por ID ---
print("\n-- SELECT reporte con id=1 --");
reporte = conexion.SelectReporteDiarioId(1);
if reporte:
    print(str(reporte.idReporte) + ", asesor:" + str(reporte.idAsesor) +
          ", cerrados:" + str(reporte.casosCerrados) + ", cumplioMeta:" + str(reporte.cumplioMeta));
 
# --- UPDATE reporte con id=1 ---
print("\n-- UPDATE reporte con id=1 --");
actualizarReporte = ReportesDiarios();
actualizarReporte.idReporte      = 1;
actualizarReporte.idAsesor       = 1;
actualizarReporte.fecha          = "2025-04-01";
actualizarReporte.casosAbiertos  = 5;
actualizarReporte.casosCerrados  = 15;
actualizarReporte.casosEnProceso = 2;
actualizarReporte.tiempoPromedio = 30.0;
actualizarReporte.cumplioMeta    = True;
conexion.UpdateReporteDiario(actualizarReporte);
print("Reporte actualizado: id=" + str(actualizarReporte.idReporte) +
      ", cerrados=" + str(actualizarReporte.casosCerrados) +
      ", cumplioMeta=" + str(actualizarReporte.cumplioMeta));
 
# --- DELETE reporte con id=5 ---
print("\n-- DELETE reporte con id=5 --");
conexion.DeleteReporteDiario(5);
print("Reporte con id=5 eliminado correctamente");
 
print("\n" + "="*60);
print("✅ PRUEBAS COMPLETADAS - 15 tablas verificadas");
print("="*60);