# Author: Nicolás Balboni
# Date: 10/27/2022
# Name: El Juego del AH_RCA_O

# Previo
import random
# lpaneque: Entiendo que este es el juego final, cierto?

# Funciones
# Comprobar posiciones acertadas (EN PROCESO)
def comprobar(intento,deletreo):
    posiciones=[]
    num=0
    for letra in deletreo:
        if intento == letra:
            posiciones.append(num)
            num=num+1
        else:
            num=num+1
    return posiciones

palabraPintada=[]
def pintarPalabra(palabra,prueba):
    seguir=True
    
    num=0
    while seguir==True:
        if num in prueba:
            palabraPintada.append(palabra[num])
            num=num+1
        elif num > len(palabra)-1:
            seguir=False
        else:
            palabraPintada.append("_")
            num=num+1

    return palabraPintada

#Comienzo del script
# Genero palabra
palabras=("PERRO","GATO","COCHE","PYTHON","SISTEMA","PROGRAMA")
palabra=random.choice(palabras)

# Desglosar la palabra
deletreo=[]  # lpaneque: Puedes convertir el string a list con list(palabra)
for letra in palabra:
    deletreo.append(letra)

# Vamos a dejar aqui esto para comprobar que todo va bien durante el proceso
print(deletreo)

# Presentación del juego
print("-----:VAMOS A JUGAR AL AH_RCA_O:-----") # lpaneque: Mola

# Pedir letra al jugador
intento=input("Escribe una letra (en MAYUSCULAS): ") # lpaneque: la puedes convertir tú con upper(letra) y así te aseguras.

# Compruebo que la letra(intento) elegida por el jugador está en la palabra
if intento in deletreo:
    print("Bien")
    
    prueba=comprobar(intento,deletreo)
    print(prueba)

    final=pintarPalabra(palabra,prueba)
    print(final)


else:
    print("Mal")
    
# lpaneque: Te faltaría incluir esto en un bucle que se repita mientras no tengas 6 fallos, puedes guardar los fallos en una variable fallos.
# lpaneque: Puedes utilizar esa variable fallos para imprimir el ahorcado correspondiente que está en una lista, ahorcado[0] sería la posición inicial,
# lpaneque: ahorcado[1] sería la siguiente y así hasta llegar a la última que creo recordar que era ahorcado[6]
