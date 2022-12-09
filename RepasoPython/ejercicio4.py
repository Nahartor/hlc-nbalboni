# Author: Nicolás Balboni
# Date: 12/12/2022
# Name: Repaso Python - Ejercicio 4

#Preparación del programa y definicion de variables globales
import sys
numeros=input("Introduzca el número de su DNI: ")
letra=input("Introduzca la letra de su DNI: ")
dni=f"{numeros}{letra}"
evalNumeros=["0","1","2","3","4","5","6","7","8","9"]
evalLetras={"T":0,"R":1,"W":2,"A":3,"G":4,"M":5,"Y":6,"F":7,"P":8,"D":9,"X":10,"B":11,"N":12,"J":13,"Z":14,"S":15,"Q":16,"V":17,"H":18,"L":19,"C":20,"K":21,"E":22}

#Definición de funciones:

#Esta función comprueba que la longitud del DNI sea correcta.
def checkLen (dni):
    if len(dni) != 9:
        print("El DNI debe tener 9 caracteres.")
        sys.exit(1)

    return

#Esta función comprueba que los 8 primeros caracteres sean números.
def checkNum(numeros):
    correcto=True
    for i in range(0,8):
        if numeros[i] not in evalNumeros:
            correcto=False

    if correcto==False:
        print("Los caracteres del 1 al 8 deben ser números")
        sys.exit(1)

    return

#Esta función comprueba que el DNI introducido no se encuentre en la lista indicada por la administración de DNIs no válidos.
def checkAdministracion (dni):
    prohibidos=["00000000T","00000001R","99999999R"]
    if dni in prohibidos:
        print("El DNI introducido no es válido.")
        sys.exit(1)

    return

#Esta función comprueba que la letra del DNI corresponda con los números en base al algoritmo.
def checkLetra(numeros,letra):
    if evalLetras[letra]!=(int(numeros)%23):
        print("La letra del DNI es incorrecta.")
        sys.exit(1)

    return

#Llamamos a las funciones por orden.
checkLen(dni)
checkNum(numeros)
checkAdministracion(dni)
checkLetra(numeros,letra)

#Si ninguna de las funciones encuentra un error que finalice el programa, lanzamos un mensaje por pantalla indicando que el formato del DNI es correcto.
print("El formato del DNI es correcto.")

#Un problema que le encuentro a mi método es que no es capaz de evaluar varios fallos simultaneamente. Ya que, cuando encuentra el primer fallo, finaliza el programa.