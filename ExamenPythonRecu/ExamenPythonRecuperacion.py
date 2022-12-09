#Ejercicio1
"""
# Author: Nicolás Balboni
# Date: 12/02/2022
# Name: Examen Python Recuperación. Ejercicio 1

def ejercicio1(palabra):
    lista1=[]
    for letra in palabra:
        lista1.append(letra)

    #print(lista1)

    lista2=[]
    longitudLista=len(lista1)
    #print(longitudLista)
    for posicion in lista1:
        lista2.append(lista1[(longitudLista)-1])
        longitudLista-=1

    #print(lista2)

    p1=str(lista1)
    p2=str(lista2)

    if p1 == p2:
        return True

    else:
        return False

palabra=input("Introduce una palabra: ")
if ejercicio1(palabra):
    print("Resultado: True")

else:
    print("Resultado: False")
"""

#Ejercicio 2
"""
# Author: Nicolás Balboni
# Date: 12/02/2022
# Name: Examen Python Recuperación. Ejercicio 2

#Cabecera
print("*****************************EJERCICIO 2******************************")
print("______________________________________________________________________")

import csv
archivo="/home/nbalboni/github/hlc-nbalboni/ExamenPythonRecu/distanciasAndalucia.csv"
ciudades=[]

#Cargamos las ciudades a una lista de diccionario
try:
    with open(archivo, 'r') as File:
        reader = csv.DictReader(File)
        for row in reader:
            ciudades.append(row)

except FileNotFoundError:
    print(f"El archivo {archivo} no existe, no se han podido cargar los nombres.")
except:
    print("Se ha producido un error inesperado.")
else:
    for i in range(49):
        print(f"Origen: {ciudades[i]['origen']} - Destino: {ciudades[i]['destino']} - Km: {ciudades[i]['km']}")
"""
#Ejercicio 3
"""
print("*****************************EJERCICIO 3******************************")
print("______________________________________________________________________")

import csv
archivo="/home/nbalboni/github/hlc-nbalboni/ExamenPythonRecu/distanciasAndalucia.csv"
ciudades=[]

#Cargamos las ciudades a una lista de diccionario
try:
    with open(archivo, 'r') as File:
        reader = csv.DictReader(File)
        for row in reader:
            ciudades.append(row)

except FileNotFoundError:
    print(f"El archivo {archivo} no existe, no se han podido cargar los nombres.")
except:
    print("Se ha producido un error inesperado.")
else:
    ciudad1=input("Introduce la ciudad de origen: ")
    ciudad2=input("Introduce la ciudad de destino: ")
    for i in range(49):
        origen=ciudades[i]['origen']
        if origen == ciudad1:
            destino=ciudades[i]['destino']
            if destino == ciudad2:
                km=ciudades[i]['km']

    #print(km)

    precios_por_litro={'diesel': 1.74, 'diesel+': 1.82, 'gasolina95': 1.64, 'gasolina98': 1.69, 'biodiesel': 1.71}
    combustible=input("Introduce el tipo de combustible: ")
    precioCombustible=precios_por_litro[combustible]
    #print(precioCombustible)

    consumo=input("¿Cuantos litros consume su vehiculo cada 100km?: ")
    #print(consumo)

    litrosConsumidos=((int(km)*float(consumo))/100)
    #print(litrosConsumidos)
    precioFinal=litrosConsumidos*precioCombustible
    #print(precioFinal)
    precioFinalRedondeado= round(precioFinal, 2)

    print(f"La distancia entre {ciudad1} y {ciudad2} es de {km}. Tu vehiculo consumirá {litrosConsumidos} litros de {combustible}. El coste del viaje será de {precioFinalRedondeado}€.")
"""