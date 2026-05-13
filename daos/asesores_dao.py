from conexion.conexion import Conexion;
from conexion.encriptacion import encriptar, desencriptar;
from modelos.asesores_modelo import ( Asesores);

class AsesoresDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;
    
    # ----------------------------------------------------------
    # ASESORES - SELECT todas
    # ----------------------------------------------------------
    def SelectAsesores(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_asesores()}");

        listaAsesores: list = [];
        for fila in cursor:
            asesor = Asesores();
            asesor.idAsesor     = fila[0];
            asesor.cedula       = desencriptar(fila[1]);
            asesor.nombre       = desencriptar(fila[2]);
            asesor.email        = desencriptar(fila[3]);
            asesor.telefono     = desencriptar(fila[4]);
            asesor.idArea       = fila[5];
            asesor.idCargo      = fila[6];
            asesor.fechaIngreso = fila[7];
            asesor.activo       = fila[8];
            listaAsesores.append(asesor);

        cursor.close();
        con.close();
        return listaAsesores;


    # ----------------------------------------------------------
    # ASESORES - SELECT por ID
    # ----------------------------------------------------------
    def SelectAsesorId(self, idAsesor: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_asesor_id(?)}", idAsesor);

        asesor = None;
        for fila in cursor:
            asesor = Asesores();
            asesor.idAsesor     = fila[0];
            asesor.cedula       = desencriptar(fila[1]);
            asesor.nombre       = desencriptar(fila[2]);
            asesor.email        = desencriptar(fila[3]);
            asesor.telefono     = desencriptar(fila[4]);
            asesor.idArea       = fila[5];
            asesor.idCargo      = fila[6];
            asesor.fechaIngreso = fila[7];
            asesor.activo       = fila[8];

        cursor.close();
        con.close();
        return asesor;

    # ----------------------------------------------------------
    # ASESORES - INSERT
    # ----------------------------------------------------------
    def InsertAsesor(self, asesor: Asesores) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_asesor(?, ?, ?, ?, ?, ?, ?, ?)}",
            encriptar(asesor.cedula),
            encriptar(asesor.nombre),
            encriptar(asesor.email),
            encriptar(asesor.telefono),
            asesor.idArea,
            asesor.idCargo,
            asesor.fechaIngreso,
            asesor.activo
        );
        con.commit();
        cursor.close();
        con.close();


    # ----------------------------------------------------------
    # ASESORES - UPDATE
    # ----------------------------------------------------------
    def UpdateAsesor(self, asesor: Asesores) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_asesor(?, ?, ?, ?, ?, ?, ?, ?, ?)}",
            asesor.idAsesor,
            encriptar(asesor.cedula),
            encriptar(asesor.nombre),
            encriptar(asesor.email),
            encriptar(asesor.telefono),
            asesor.idArea,
            asesor.idCargo,
            asesor.fechaIngreso,
            asesor.activo
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # ASESORES - DELETE
    # ----------------------------------------------------------
    def DeleteAsesor(self, idAsesor: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_asesor(?)}", idAsesor);
        con.commit();
        cursor.close();
        con.close();