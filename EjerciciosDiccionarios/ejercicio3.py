# Author: Nicolás Balboni
# Date: 10/27/2022
# Name: EJERCICIOS DE DICCIONARIOS EN PYTHON - Ejercicio 3

from email.mime import base
from pickletools import int4


verduras={"Cebolla":1.30,"Patata":0.90,"Tomate":1.59,"Berenjena":1.25}

producto=input("Introduzca un producto: ")
kilos=input("Introduzca el número de kilos: ")

base=verduras.get(producto)
precio=base*float(kilos)

print(f"El precio total de su compra es: {precio}.")