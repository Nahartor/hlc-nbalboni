# Author: Nicolás Balboni
# Date: 10/20/2022
# Name: OBLIGATORIA P1 E2. Adivina el número.

import random

# Definimos funciones
def extraer_num(cadena): # lpaneque: Esta función ya existe en Python, se llama list(cadena) y lo que hace es convertir una cadena de texto en lista.
    num=[]
    for i in str(cadena):
        num.append(int(i))

    return num

# Gerneramos número aleatorio
numero_secreto=random.randint(1000,9999)

#Comienzo del script
seguir=True
while seguir:
    numero_jugador=input("Intenta adivinar el código secreto: ")

    cadena_secreto=extraer_num(numero_secreto) # Esto es una acción repetitiva, imagina que tienes que comparar 100 números, sería mejor utilizar un bucle
    num_sec_1=cadena_secreto[0]
    num_sec_2=cadena_secreto[1]
    num_sec_3=cadena_secreto[2]
    num_sec_4=cadena_secreto[3]

    cadena_jugador=extraer_num(numero_jugador)
    num_jug_1=cadena_jugador[0]
    num_jug_2=cadena_jugador[1]
    num_jug_3=cadena_jugador[2]
    num_jug_4=cadena_jugador[3]
    
    # Para el bucle que te he comentado antes podrías hacer algo así:
    # acertado = True
    # for i in range (0, length(cadena_secreto)):
    #   if cadena_secreto[i] != cadena_jugador[i]:
    #       acertado = False
    #       break
    # if acertado:
    #   print("ACERTADO")

    # ¿Ganaste?

    if num_jug_1==num_sec_1 and num_jug_2==num_sec_2 and num_jug_3==num_sec_3 and num_jug_4==num_sec_4:
        print("¡HAS ACERTADO!")
        seguir=False

    # Parece que no, te doy una pista.
    else:
        # Primer número
        if num_jug_1==num_sec_1: # Este if está repetido cuatro veces, podrías meterlo en una función a la que le pasas dos números y te dice si te has pasado o te has quedado corto.
            print("¡Enhorabuena! El primer número coincide.")

        elif num_jug_1>num_sec_1:
            print("Primer número: Te has pasado.")

        elif num_jug_1<num_sec_1:
            print("Primer número: Te has quedado corto.")

        # Segundo número
        if num_jug_2==num_sec_2:
            print("¡Enhorabuena! El segundo número coincide.")

        elif num_jug_2>num_sec_2:
            print("Segundo número: Te has pasado.")

        elif num_jug_2<num_sec_2:
            print("Segundo número: Te has quedado corto.")

        # Tercer número
        if num_jug_3==num_sec_3:
            print("¡Enhorabuena! El tercer número coincide.")

        elif num_jug_3>num_sec_3:
            print("Tercer número: Te has pasado.")

        elif num_jug_3<num_sec_3:
            print("Tercer número: Te has quedado corto.")

        # Cuarto número
        if num_jug_4==num_sec_4:
            print("¡Enhorabuena! El cuarto número coincide.")

        elif num_jug_4>num_sec_4:
            print("Cuarto número: Te has pasado.")

        elif num_jug_4<num_sec_4:
            print("Cuarto número: Te has quedado corto.")
    
        opcion=input("¿Quieres probar otra vez? [Y/N]")

        # ¿Continue?
        op=True   
        while op:
            if opcion=="Y" or opcion=="y":
                seguir=True
                op=False
            elif opcion=="N" or opcion=="n":
                seguir=False
                op=False
            else:
                print("Opción Incorrecta")
