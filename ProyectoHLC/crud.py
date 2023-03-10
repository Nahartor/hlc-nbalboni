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
        return f"Asignatura con nombre {self.nombre} impartida por el profesor/a {self.profesor}"
    
class Alumno:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"Nombre alumno: {self.apellidos}, {self.nombre}.\ne-mail: {self.email}"
    
class UsersDBConnection(DatabaseConnection):

    def insertar_asignatura(self,nombre, profesor):
        self.get_cursor().execute("insert into asignaturas (nombre,profesor) values(?,?)", (nombre,profesor))
        self.conn.commit()

    def listar_asignaturas(self):
        asignaturas = []
        cur=self.get_cursor()
        cur.execute("select * from asignaturas")
        for (idasig,nombre,profesor) in cur:
            asignaturas.append(Asignatura(idasig,nombre,profesor))
        return asignaturas
    
    def get_alum_by_name(self, nombre, apellidos):
        cur = self.get_cursor()
        cur.execute("select id, nombre, apellidos, email from alumnos where ((nombre LIKE ?) and (apellidos LIKE ?))",(nombre, apellidos))
        for (id, nombre, apellidos, email) in cur:
            return Alumno(id, nombre, apellidos, email)
    
    def get_asig_by_name(self, nombre):
        cur = self.get_cursor()
        cur.execute("Select idasig, nombre, profesor from asignaturas where nombre LIKE ?",(nombre,))
        for (idasig, nombre, porfesor) in cur:
            asignatura=Asignatura(idasig, nombre, porfesor)
            return asignatura#Asignatura(idasig, nombre, porfesor)

    def update_asig_by_name(self, nombre, campo, valor):
        cur = self.get_cursor()
        if campo == "profesor":
            cur.execute("update asignaturas set profesor = ? where nombre= ?",(valor,nombre))

        else:
            cur.execute("update asignaturas set nombre = ? where nombre= ?",(valor,nombre))
        
        self.conn.commit()

    def delete_asig_by_name(self,nombre):
        cur = self.get_cursor()
        cur.execute("delete from asignaturas where nombre= ?",(nombre,))
        self.conn.commit()


if __name__ == "__main__":
    # Creando la conexión a la base de datos
    user_conn = UsersDBConnection("172.26.0.34",3306,"fulanito","instituto","1234")
    user_conn.connect()

    def insert():
        print("INSERTANDO UNA NUEVA ASIGNATURA -->")
        new_asig = input("Introduce el nombre de la asignatura que deseas guardar: ")
        proff= input("Introduce el nombre del profesor que imparte dicha asignatura: ")
        user_conn.insertar_asignatura(new_asig,proff)
    
    def select_all():
        print ("LISTANDO ASIGNATURAS -->")
        asignaturas=user_conn.listar_asignaturas()
        for asignatura in asignaturas:
            print(asignatura)
    
    def select_by_name():
        print("BUSCANDO UN ASIGNATURA POR NOMBRE --> ")
        nombre = input("Introduce el nombre de la asignatura que deseas buscar: ")
        asig = user_conn.get_asig_by_name(nombre)
        print(asig)
    
    def update():
        print("MODIFICANDO UNA ASIGNATURA -->")
        nombre = input("Introduce el nombre de la asignatura que deseas modificar: ")
        campo = input("Introduce el campo que deseas modificar en la asignatura (nombre/profesor): ")
        valor= input("Introduce el nuevo valor para el campo que deseas modificar: ")
        user_conn.update_asig_by_name(nombre,campo,valor)
        asig= user_conn.get_asig_by_name(nombre)
        print(asig)

    def delete():
        print("BORRANDO UNA ASIGNATURA --> ")
        nombre = input("Introduce el nombre de la asignatura que deseas eliminar: ")
        print("A continuación se muestran los datos de la asignatura seleccionada: ")
        asig= user_conn.get_asig_by_name(nombre)
        print(asig)
        confirmacion = input("¿Seguro que deseas elminar esta asignatura de la base de datos? (s/n): ")
        if confirmacion == "s":
            user_conn.delete_asig_by_name(nombre)

        else:
            print("Operación cancelada a petición suya.\nNo se ha eliminado ningún campo.")

    # Menú
    print("Selecciona una de las siguientes opciones:")
    print("1. Insertar una nueva asignatura.\n2. Mostrar todas las asignatras.\n3. Mostrar una asignatura filtrada por nombre.\n4. Modificar un campo de una asignatura.\n5. Borrar una asignatura.")
    opcion = input("¿Que acción deseas realizar?: ")

    if opcion == "1":
        insert()

    elif opcion == "2":
        select_all()

    elif opcion == "3":
        select_by_name()

    elif opcion == "4":
        update()

    elif opcion == "5":
        delete()

    else: 
        print("La opción introducida no es correcta.")
        sys.exit(1)


    # Cerrando la conexión 
    user_conn.close()

    
