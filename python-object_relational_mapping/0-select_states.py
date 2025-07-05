#!/usr/bin/python3
"""Lista todos los estados de la base de datos hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Crear cursor y ejecutar consulta
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Obtener resultados y mostrar
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Cerrar conexiones
    cur.close()
    db.close()