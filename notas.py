# Author: nbalboni

# Date: 09/29/2022

nota=float(input("Introduce la nota del alumno: "))

print(f"La nota introducida es: {nota}")

if 0 <= nota < 5:
    resultado = "Insuficiente"
elif 5 <= nota < 6:
    resultado = "Suficiente"
elif 6 <= nota < 7:
    resultado = "Bien"
elif 7 <= nota < 9:
    resultado = "Notable"
elif 9 <= nota < 10:
    resultado = "Sobresaliente"
elif nota == 6:
    resultado = "Matrícula de Honor"
else:
    resultado = "Nota no válida."

print(f"La calificación corresponiente es: {resultado}")