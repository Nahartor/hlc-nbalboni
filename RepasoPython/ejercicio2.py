# Author: Nicolás Balboni
# Date: 12/12/2022
# Name: Repaso Python - Ejercicio 2

def convierteTiempo (segundos):
    horas=segundos//3600
    minutos= (segundos%3600)//60
    segundos2=segundos-((horas*3600)+(minutos*60))
    print(f"{segundos} segundos es igual a: {horas} horas, {minutos} minutos y {segundos2} segundos.")
    
    return


print("El siguiente programa convierte segundos a horas, minutos y segundos.")
segundos=int(input("Introduzca el tiempo en segundos: "))
convierteTiempo(segundos)
