from crud import DatabaseConnection, UsersDBConnection, Asignatura
# Creando la conexión a la base de datos
user_conn = UsersDBConnection("172.26.0.34",3306,"fulanito","instituto","1234")
user_conn.connect()

def get_db():
    return user_conn