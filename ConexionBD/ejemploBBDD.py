import mariadb
import sys

# Crear la conexion a la base de datos
try:
    conn = mariadb.connect(
        user="fulanito",
        password="1234",
        host="172.26.0.34",
        port=3306,
        database="instituto"

    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Crear cursor
cur = conn.cursor()

try:
    cur.execute("INSERT INTO alumnos (nombre,apellidos,email) VALUES ('Mario','Vaquerizo','mvaquerizo@ciudadjardin.org')")
    conn.commit()
except mariadb.Error as e:
    print(f"Error al insertar en la bbdd {e}")

cur.execute("SELECT * FROM alumnos")
for (id,nombre,apellidos,email) in cur:
    print(f"ID: {id}\nNombre: {nombre}\nApellidos: {apellidos}\nEmail: {email}")

# Cerrar conexion
conn.close()