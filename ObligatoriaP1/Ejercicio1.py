# Author: Nicolás Balboni
# Date: 10/13/2022
# Name: OBLIGATORIA P1 E1. Piedra, papel, tijera (lagarto, Spock)
import random
from ast import Return

# Vamos a transformar la eleccion del usuario a número.
def texto_a_num(j1=""):
    num=0
    min=j1.lower()
    if min == "spock":
        num=1
    elif min == "tijeras":
        num=2
    elif min == "papel":
        num=3
    elif min == "piedra":
        num=4
    elif min == "lagarto":
        num=5
    else:
        print("Tu elección no es válida.")

    return num

# Comienzo del script
print("Juguemos a piedra, papel, tijeras, lagarto, Spock.")
j1=(input("Introduce tu elección: "))   

entrada_usuario=texto_a_num()
print(entrada_usuario)
numero_aleatorio =random.randint(1,5)
print(numero_aleatorio)

gana = {1:[2,4], 2:[3,5], 3:[1,4], 4:[2,5], 5:[1,3]}

if entrada_usuario in gana.pop(numero_aleatorio):
    print("Gana la máquina.")
elif entrada_usuario == numero_aleatorio:
    print("¡EMPATE!")

else:
    print("¡Has ganado!")
