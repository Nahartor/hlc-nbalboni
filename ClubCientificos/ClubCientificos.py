# Author: Nicolás Balboni
# Date: 12/14/2022
# Name: Manejo CSV
import csv

#Guardamos el CSV en memoria
archivo="/home/nbalboni/github/hlc-nbalboni/ClubCientificos/ClubCientificos.csv"
cientificos=[]

with open(archivo, 'r') as File:
    reader = csv.DictReader(File)
    for row in reader:
        cientificos.append(row)

#Creamos una función que muestre los datos por pantalla:
def mostrarDatos():
    for i in range(int(len(cientificos))):
        print(f"Nº de socio: {cientificos[i]['Socio']} - Nombre: {cientificos[i]['Nombre']} - Apellido: {cientificos[i]['Apellido']} - Nacimiento: {cientificos[i]['Nacimiento']} - Muerte: {cientificos[i]['Muerte']} - Campo: {cientificos[i]['Campo']}")

def buscarPorClave():
    num=input("Introduce el número de socio: ")
    for i in range(int(len(cientificos))):
        socio=cientificos[i]['Socio']
        if socio == num:
            print(f"Nº de socio: {cientificos[i]['Socio']} - Nombre: {cientificos[i]['Nombre']} - Apellido: {cientificos[i]['Apellido']} - Nacimiento: {cientificos[i]['Nacimiento']} - Muerte: {cientificos[i]['Muerte']} - Campo: {cientificos[i]['Campo']}")

def añadirSocio():
    print("A continuación vamos a introducir los datos del nuevo socio...")
    socio=input("Introduce un número de socio: ")
    nombre=input("Introduce el nombre del socio: ")
    apellido=input("Introduce el apellido de socio: ")
    nacimiento=input("Introduce la fecha de nacimiento del socio (en formato DD-MM-AAAA): ")
    muerte=input("Introduce la fecha de defunción del socio (en formato DD-MM-AAAA)\n En caso de seguir vivo deje este campo en blanco: ")
    campo=input("Introduce el campo de estudio del socio: ")

    #nuevoSocio=str(f"{socio},{nombre},{apellido},{nacimiento},{muerte},{campo}")

    

    nuevoSocio={"Socio":socio, "Nombre":nombre, "Apellido":apellido, "Nacimiento":nacimiento, "Muerte":muerte, "Campo":campo}
    cientificos.append(nuevoSocio)


def borrarSocio():
    num=input("Introduce el número de socio: ")
    for i in cientificos:
        socio=i['Socio']
        if socio == num:
            cientificos.remove(i)


def modificarSocio():
    num=input("Introduce el número de socio: ")
    calve=input("Introduzca el parámetro que desea modificar (primera letra en Mayúscula): ")
    for i in cientificos:
        socio=i['Socio']
        if socio == num:
            entrada=input("Introduzca el nuevo valor: ")
            nuevo={calve:entrada}
            i.update(nuevo)




def sobreescribirCSV():
    header=["Socio","Nombre","Apellido","Nacimiento","Muerte","Campo"]
    with open(archivo, 'w', newline='') as File:
        writer= csv.DictWriter(File,header)
        writer.writeheader()
        writer.writerows(cientificos)

#Menú
salir=False
while salir==False:
    print("Elija una de las siguientes opciones...")
    print("1-Mostrar los datos de todos los socios.")
    print("2-Mostrar los datos de un socio concreto (filtrado por su nº de socio).")
    print("3-Añadir un socio nuevo.")
    print("4-Borrar un socio (filtrado por su nº de socio).")
    print("5-Modificar un campo concreto de un socio.")
    print("6-Guardar y salir")
    print("7-Salir sin guardar.")
    opcion=input("Escriba la opción correspondiente ==> ")

    if opcion=="1":
        mostrarDatos()

    elif opcion=="2":
        buscarPorClave()

    elif opcion=="3":
        añadirSocio()
        mostrarDatos()

    elif opcion=="4":
        borrarSocio()
        mostrarDatos()

    elif opcion=="5":
        modificarSocio()
        mostrarDatos()

    elif opcion=="6":
        print("¡Hasta luego!")
        sobreescribirCSV()
        salir=True

    elif opcion=="7":
        print("¡Hasta luego!")
        salir=True