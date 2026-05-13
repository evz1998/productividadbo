#Librerias

import pyodbc;

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
    
    def conectar(self):
        return pyodbc.connect(self.strConnection);