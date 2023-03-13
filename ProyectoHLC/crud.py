import sys
from  mariadb import connect, Error

host="172.26.0.34"#casa"localhost"
port=3306#casa10307
user="fulanito"
database="instituto"
password="1234"

conn = connect(host=host, port=port, user=user, database=database, password=password)

class Asignatura:
    def __init__(self, profesor, nombre= None, idasig= None):
        self.idasig = idasig
        self.nombre = nombre
        self.profesor = profesor

    def insertar_asignatura(self):
        cur= conn.cursor()
        nombre=self.nombre
        profesor=self.profesor
        cur.execute("insert into asignaturas (nombre,profesor) values(?,?)", (nombre,profesor))
        conn.commit()

    def update_asig_by_id(self,idasig):
        cur = conn.cursor()
        cur.execute("update asignaturas set profesor = ? where idasig= ?",(self.profesor,idasig))
        conn.commit()


    def __str__(self):
        return f"Asignatura con nombre {self.nombre} impartida por el profesor/a {self.profesor}"
       
def listar_asignaturas():
    asignaturas = []
    cur=conn.cursor()
    cur.execute("select * from asignaturas")
    for (idasig,nombre,profesor) in cur:
        asignaturas.append(Asignatura(idasig=idasig,nombre=nombre,profesor=profesor))
    return asignaturas

def get_asig_by_name(nombre):
    cur = conn.cursor()
    cur.execute("Select idasig, nombre, profesor from asignaturas where nombre LIKE ?",(nombre,))
    for (idasig, nombre, profesor) in cur:
        asignatura=Asignatura(idasig=idasig, nombre=nombre, profesor=profesor)
        return asignatura#Asignatura(idasig, nombre, porfesor) 
    
def get_asig_by_id(idasig):
    cur = conn.cursor()
    cur.execute("Select idasig, nombre, profesor from asignaturas where idasig LIKE ?",(idasig,))
    for (idasig, nombre, profesor) in cur:
        asignatura=Asignatura(idasig=idasig, nombre=nombre, profesor=profesor)
        return asignatura#Asignatura(idasig, nombre, porfesor) 

def json_to_pithon(datos):
    nueva=Asignatura(
        #idasig=datos["idasig"],
        nombre=datos["nombre"],
        profesor=datos["profesor"]
    )
    return nueva

def json_to_pithon_2(datos2):
    nueva=Asignatura(
        #idasig=datos["idasig"],
        # nombre=datos["nombre"],
        profesor=datos2["profesor"]
    )
    return nueva
    
def delete_asig_by_id(idasig):
    cur = conn.cursor()
    cur.execute("delete from asignaturas where idasig= ?",(idasig,))
    conn.commit()
