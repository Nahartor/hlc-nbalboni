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
                user=self.user,#hlc",
                password=self.password,#"1234",
                host=self.host,#"localhost",
                port=self.port,#3306,
                database=self.database#"prueba"
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

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Usuario con id {self.id} y nombre {self.name}"
    
class UsersDBConnection(DatabaseConnection):

    def insert_user(self,id, name):
        self.get_cursor().execute("insert into usuarios values(?,?)", (id,name))
        self.conn.commit()

    def list_users(self):
        users = []
        cur=self.get_cursor()
        cur.execute("select * from usuarios")
        for (id,name) in cur:
            users.append(User(id,name))
        return users
    
    def get_user_by_id(self, id):
        cur = self.get_cursor()
        cur.execute("Select id, name from usuarios where id = ?",(id,))
        for (id, name) in cur:
            return User(id, name)


if __name__ == "__main__":
    # Creando la conexión a la base de datos
    user_conn = UsersDBConnection("127.0.0.1",3306,"hlc","prueba","1234")
    user_conn.connect()


    print("INSERTANDO UN NUEVO USUARIO -->")
    new_user = input("Introduce el nombre del usuario que deseas guardar: ")


    print ("LISTANDO USUARIOS -->")
    usuarios=user_conn.list_users()
    for usuario in usuarios:
        print(usuario)

    print("BUSCANDO UN USUARIO POR ID --> ")
    id = input("Introduce el id del usuario que deseas buscar: ")
    user = user_conn.get_user_by_id(id)
    print(user)

    # Cerrando la conexión 
    user_conn.close()

    
