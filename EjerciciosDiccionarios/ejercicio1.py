# Author: Nicolás Balboni
# Date: 10/20/2022
# Name: EJERCICIOS DE DICCIONARIOS EN PYTHON - Ejercicio 1

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
telefono = input("Introduce tu teléfono: ")
direccion = input("Introduce tu dirección: ")

datos_personales = {"Nombre": nombre, "edad": edad, "Teléfono": telefono, "Dirección": direccion }

print(f"{datos_personales['Nombre']} tiene {datos_personales['edad']} años, vive en {datos_personales['Dirección']} y su teléfono es {datos_personales['Teléfono']}")