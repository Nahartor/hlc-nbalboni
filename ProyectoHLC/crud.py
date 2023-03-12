import sys
from  mariadb import connect, Error

host="localhost"
port=10307
user="fulanito"
database="instituto"
password="1234"

conn = connect(host=host, port=port, user=user, database=database, password=password)

class Asignatura:
    def __init__(self, nombre, profesor, idasig= None):
        self.idasig = idasig
        self.nombre = nombre
        self.profesor = profesor

    def insertar_asignatura(self):
        cur= conn.cursor()
        #idasig=self.idasig
        nombre=self.nombre
        profesor=self.profesor
        cur.execute("insert into asignaturas (nombre,profesor) values(?,?)", (nombre,profesor))
        conn.commit()

    def update_asig_by_id(self):
        idasig=self.idasig
        profesor=self.profesor
        cur = conn.cursor()
        cur.execute("update asignaturas set profesor = ? where idasig= ?",(profesor,idasig))
        conn.commit()


    def __str__(self):
        return f"Asignatura con nombre {self.nombre} impartida por el profesor/a {self.profesor}"
    

       
def listar_asignaturas():
    asignaturas = []
    cur=conn.cursor()
    cur.execute("select * from asignaturas")
    for (idasig,nombre,profesor) in cur:
        asignaturas.append(Asignatura(idasig,nombre,profesor))
    return asignaturas

def get_asig_by_name(nombre):
    cur = conn.cursor()
    cur.execute("Select idasig, nombre, profesor from asignaturas where nombre LIKE ?",(nombre,))
    for (idasig, nombre, porfesor) in cur:
        asignatura=Asignatura(idasig, nombre, porfesor)
        return asignatura#Asignatura(idasig, nombre, porfesor) 
    
def get_asig_by_id(idasig):
    cur = conn.cursor()
    cur.execute("Select idasig, nombre, profesor from asignaturas where idasig LIKE ?",(idasig,))
    for (idasig, nombre, porfesor) in cur:
        asignatura=Asignatura(idasig, nombre, porfesor)
        return asignatura#Asignatura(idasig, nombre, porfesor) 

"""    
def insertar_asignatura(nombre, profesor):
    conn.cursor().execute("insert into asignaturas (nombre,profesor) values(?,?)", (nombre,profesor))
    conn.commit()
"""

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
    
def update_asig_by_name(nombre, campo, valor):
    cur = conn.cursor()
    if campo == "profesor":
        cur.execute("update asignaturas set profesor = ? where nombre= ?",(valor,nombre))

    else:
        cur.execute("update asignaturas set nombre = ? where nombre= ?",(valor,nombre))
    
    conn.commit()


def delete_asig_by_name(self,nombre):
    cur = conn.cursor()
    cur.execute("delete from asignaturas where nombre= ?",(nombre,))
    conn.commit()

def delete_asig_by_id(idasig):
    cur = conn.cursor()
    cur.execute("delete from asignaturas where idasig= ?",(idasig,))
    conn.commit()

json= {"nombre":"FOL", "profesor":"Irene"} 
prueba= json_to_pithon(json)


# prueba.insertar_asignatura()