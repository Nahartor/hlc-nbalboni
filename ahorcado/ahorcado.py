# Author: Nicolás Balboni
# Date: 10/27/2022
# Name: El Juego del AH_RCA_O

# Previo
import random

# Funciones
    # Comprobar posiciones acertadas (EN PROCESO)
def comprobar(intento,desglose):
    posiciones=[]

    for posicion in desglose:
        if intento == posicion:
            posiciones.append(num)
            num=num+1

        elif desglose[3]:
            seguir=False

        else:
            num=num+1

    return posiciones


#Comienzo del script
# Genero palabra
palabras=("PERRO","GATO","COCHE","PYTHON","SISTEMA","PROGRAMA")
palabra=random.choice(palabras)

# Desglosar la palabra
desglose=[]
for letra in palabra:
    desglose.append(letra)

# Vamos a dejar aqui esto para comprobar que todo va bien durante el proceso
print(desglose)

# Presentación del juego
print("-----:VAMOS A JUGAR AL AH_RCA_O:-----")

# Pedir letra al jugador
intento=input("Escribe una letra (en MAYUSCULAS): ")

# Compruebo que la letra(intento) elegida por el jugador está en la palabra
if intento in desglose:
    print("Bien")
    prueba=comprobar(intento,desglose)

    print(prueba)


else:
    print("Mal")