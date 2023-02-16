import sys
from  mariadb import connect, Error

class DatabaseConnection:

    def __init__(self, host, port, user, database, password):
        self.host = host
        self.port = port
        self.user = user
        self.database = database
        self.password = password
        self.conn = None

    def connect(self):

        try:
            self.conn=connect(
                user=self.user,#"fulanito",
                password=self.password,#"1234",
                host=self.host,#"172.26.0.34",
                port=self.port,#3306,
                database=self.database#"instituto"
            )
        except Error as e:
            print(f"Error connecting to database {e}")
            sys.exit(1)
        else:
            print("Conexión realizada a la base de datos.")

    def close(self):
        self.conn.close()

    def execute_query(self,query):
        self.conn.cursor().execute(query)

    def get_cursor(self):
        return self.conn.cursor()

class Asignatura:
    def __init__(self, idasig, nombre, profesor):
        self.idasig = idasig
        self.nombre = nombre
        self.profesor = profesor

    def __str__(self):
        return f"Asignatura con nombre {self.nombre} impartida por el profesor {self.profesor}"
    
class UsersDBConnection(DatabaseConnection):

    def insertar_asignatura(self,nombre, profesor):
        self.get_cursor().execute("insert into asignaturas (nombre,profesor) values(?,?)", (nombre,profesor))
        self.conn.commit()

    def listar_asignaturas(self):
        asignaturas = []
        cur=self.get_cursor()
        cur.execute("select * from asignaturas")
        for (nombre,profesor) in cur:
            asignaturas.append(Asignatura(nombre,profesor))
        return asignaturas
    
    def get_asig_by_name(self, nombre):
        cur = self.get_cursor()
        cur.execute("Select idasig, nombre, profesor from asignaturas where nombre LIKE ?",(nombre,))
        for (idasig, nombre, porfesor) in cur:
            return Asignatura(idasig, nombre, porfesor)


if __name__ == "__main__":
    # Creando la conexión a la base de datos
    user_conn = UsersDBConnection("172.26.0.34",3306,"fulanito","instituto","1234")
    user_conn.connect()


    print("INSERTANDO UNA NUEVA ASIGNATURA -->")
    new_asig = input("Introduce el nombre de la asignatura que deseas guardar: ")
    proff= input("Introduce el nombre del profesor que imparte dicha asignatura: ")
    user_conn.insertar_asignatura(new_asig,proff)


    print ("LISTANDO ASIGNATURAS -->")
    asignaturas=user_conn.listar_asignaturas()
    for asignatura in asignaturas:
        print(asignatura)

    print("BUSCANDO UN ASIGNATURA POR NOMBRE --> ")
    nombre = input("Introduce el nombre de la asignatura que deseas buscar: ")
    asig = user_conn.get_asig_by_name(nombre)
    print(nombre)

    # Cerrando la conexión 
    user_conn.close()

    
