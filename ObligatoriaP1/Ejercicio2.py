# Author: Nicolás Balboni
# Date: 10/20/2022
# Name: OBLIGATORIA P1 E2. Adivina el número.

import random

numero_secreto=random.randint(1000-9999)

numero_jugador=input("Intenta adivinar el código secreto: ")

def extraer_num(cadena):
    num=[]
    for i in str(cadena):
        num.append(int(i))

    return 