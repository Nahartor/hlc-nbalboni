# Author: Nicolás Balboni
# Date: 12/12/2022
# Name: Repaso Python - Ejercicio 3

clave = {"M":"0","U":"1","R":"2","C":"3","I":"4","E":"5","L":"6","A":"7","G":"8","O":"9",
         "0":"M","1":"U","2":"R","3":"C","4":"I","5":"E","6":"L","7":"A","8":"G","9":"O",
         " ":" "}

coincidencias=[] 
texto=str(input("Introduce lo que quieres codificar o decodificar (en MAYUSCULAS): "))

for letra in texto:
    if letra in clave and letra not in coincidencias:
            coincidencias.append(letra)

for i in coincidencias: 
    texto = texto.replace(i,clave[i])

print(texto)