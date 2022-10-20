# Author: Nicolás Balboni
# Date: 10/13/2022
# Name: OBLIGATORIA P1 E1. Piedra, papel, tijera (lagarto, Spock)
import random
from ast import Return

# Vamos a transformar la eleccion del usuario y de la máquina a número.
def texto_a_num(minusculas):
    num=0
    if minusculas == "spock":
        num=1
    elif minusculas == "tijeras":
        num=2
    elif minusculas == "papel":
        num=3
    elif minusculas == "piedra":
        num=4
    elif minusculas == "lagarto":
        num=5

    return num

# Con la siguiente linea le pasamos las reglas del juego al programa (se pueden accualizar a nuestra elección).
gana = {1:[2,4], 2:[3,5], 3:[1,4], 4:[2,5], 5:[1,3]}
#_________________________________________________________________________________________

# Comienzo del script
# ¿Continue?
#u_seguir="Y"
seguir=True
while seguir: 
    u_seguir="Y"   
    if u_seguir != "Y" and u_seguir != "y" and u_seguir != "N" and u_seguir != "n":
        print("Opción Incorrecta")
    elif u_seguir=="Y" or u_seguir=="y":

        # Para evitar que el usuario introduzca una opcion indeseada pasamos la entrada por teclado a traves de un filtro.
        print("Juguemos a piedra, papel, tijeras, lagarto, Spock.")
        salir=False
        while salir==False:
            
            j1=(input("Introduce tu elección: "))    
            u_minusculas=j1.lower()
            entrada_usuario=texto_a_num(u_minusculas)
            if entrada_usuario != 1 and entrada_usuario != 2 and entrada_usuario !=3 and entrada_usuario !=4 and entrada_usuario !=5:
                print("Tu elección no es válida.")
            else:
                salir=True


        #print(minusculas)
        #print(entrada_usuario)
        #numero_aleatorio =random.randint(1,5)
        #print(numero_aleatorio)

        # Generamos una eleccion para la máquina
        opciones=("piedra","papel","tijeras","lagarto","spock")
        opcion_maquina=random.choice(opciones)

        numero_aleatorio=texto_a_num(opcion_maquina)

        # Mostramos al usuario el progreso
        print(f"Has elegido:  {u_minusculas}")
        print(f"La máquina ha elegido: {opcion_maquina}")

        # Resolvemos el juego

        if entrada_usuario in gana.pop(numero_aleatorio):
            print("Gana la máquina.")
        elif entrada_usuario == numero_aleatorio:
            print("¡EMPATE!")

        else:
            print("¡Has ganado!")
        
        u_seguir=input("¿Quieres jugar otra vez? Y/N: ")

        if u_seguir=="N" or u_seguir=="n":
            seguir=False

