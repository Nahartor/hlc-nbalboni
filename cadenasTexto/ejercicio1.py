# Author: nbalboni

# Date: 09/29/2022

# Tittle: Ejercicio1

# Definimos la variable "telefono"
telefono=(input("Introduzca su número de teléfono: "))

# Mostramos en pantalla el valor almacenado en la variable.
print(f"El número de teléfono introducido es: {telefono}")

# Definimos la variable "pre" para el prefijo.
pre=telefono[0:3]

# Definimos la variable "num" para el número.
num=telefono[3:]

# Mostramos los resultados por pantalla.
print(f"El prefijo es: {pre}")
print(f"El número es: {num}")