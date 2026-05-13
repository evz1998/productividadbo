from conexion.conexion import Conexion;
from modelos.areas_modelo import (Areas)

class AreasDAO:

    def __init__(self,conexion:Conexion):
        self._conexion  = conexion;


    # ----------------------------------------------------------
    # AREAS - SELECT todas
    # ----------------------------------------------------------
    def SelectAreas(self) -> list:
        con = self._conexion.conectar();
        cursor = con.cursor();
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
        con.close();
        return listaArea;


    # ----------------------------------------------------------
    # AREAS - SELECT por ID
    # ----------------------------------------------------------
    def SelectAreaId(self, idArea: int):
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_select_area_id(?)}", idArea);

        area = None;                   # Si no encuentra nada, retorna None
        for fila in cursor:
            area = Areas();
            area.idArea      = fila[0];
            area.nomArea     = fila[1];
            area.descripcion = fila[2];
            area.activa      = fila[3];

        cursor.close();
        con.close();
        return area;


    # ----------------------------------------------------------
    # AREAS - INSERT
    # ----------------------------------------------------------
    def InsertArea(self, area: Areas) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_insert_area(?, ?, ?)}",
            area.nomArea,      # ? 1
            area.descripcion,  # ? 2
            area.activa        # ? 3
        );
        con.commit();     # Confirma los cambios en la BD
        cursor.close();
        con.close();


    # ----------------------------------------------------------
    # AREAS - UPDATE
    # ----------------------------------------------------------
    def UpdateArea(self, area: Areas) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute(
            "{CALL proc_update_area(?, ?, ?, ?)}",
            area.idArea,       # ? 1 -> id del área a modificar
            area.nomArea,      # ? 2
            area.descripcion,  # ? 3
            area.activa        # ? 4
        );
        con.commit();
        cursor.close();
        con.close();

    # ----------------------------------------------------------
    # AREAS - DELETE
    # ----------------------------------------------------------
    def DeleteArea(self, idArea: int) -> None:
        con = self._conexion.conectar();
        cursor = con.cursor();
        cursor.execute("{CALL proc_delete_area(?)}", idArea);
        con.commit();
        cursor.close();
        con.close();