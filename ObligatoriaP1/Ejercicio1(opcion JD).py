# Author: Nicolás Balboni
# Date: 10/13/2022
# Name: OBLIGATORIA P1 E1. Piedra, papel, tijera (lagarto, Spock)
import random
from ast import Return

# Vamos a transformar la eleccion del usuario a número.
def texto_a_num(j1=0):
    num=0
    salir=False
    while salir==False:
        try:
            min=j1.lower()
            # lpaneque: Esto lo podrías hacer con un diccionario {1: "spock", 2: "tijeras", 3: "papel"...
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

        except:
            print("Tu elección no es válida.") 
        else:
            print(num)
            salir=True
    return num
 
print("Juguemos a piedra, papel, tijeras, lagarto, Spock.")
j1=(input("Introduce tu elección: "))   

entrada_usuario=texto_a_num()
print(entrada_usuario) # lpaneque: Supongo que este print y el de abajo son a modo de log, pero en realidad al usuario no le dicen nada.
numero_aleatorio =random.randint(1,5) # Esto podría ir en una función llamada generar_opcion_maquina
print(numero_aleatorio)

gana = {1:[2,4], 2:[3,5], 3:[1,4], 4:[2,5], 5:[1,3]}

if entrada_usuario in gana.pop(numero_aleatorio):# lpaneque: Cuidado con el método pop. 
    # Pop elimina del diccionario la clave y el valor que estás buscando, así que la próxima vez que lo busques no lo encontrás porque no existe.
    # Utiliza get en lugar de pop
    print("Gana la máquina.") # Deberías informar qué opción ha salido en la máquina
elif entrada_usuario == numero_aleatorio:
    print("¡EMPATE!")

else:
    print("¡Has ganado!")
    
# lpaneque: Faltaría por incluir "Tras jugar una partida, deberás volver a solicitar al usuario si quiere jugar otra y así sucesivamente hasta que el usuario introduzca  no."
# Si introduces algo no válido se produce un bucle infinito mostrando "Tu elección no es válida"
