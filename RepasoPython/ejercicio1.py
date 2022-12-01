# Author: Nicolás Balboni
# Date: 12/01/2022
# Name: Repaso Python - Ejercicio 1

def detecta_anagrama(palabra1,palabra2):
    lista_letras=[]
    for letra in palabra1:
        lista_letras.append(letra)

    #print(lista_letras)

    es_igual=True
    for i in range(0,len(lista_letras)):
        if lista_letras[i] in palabra2:
            i+=1
        else: 
            es_igual=False

    return es_igual

palabra1=input("Introduce la primera palabra: ")
palabra2=input("Introduce la segunda palabra: ")
if detecta_anagrama(palabra1,palabra2) == True:
    print(f"{palabra1} y {palabra2} son anagramas.")

else:
    print(f"{palabra1} y {palabra2} no son anagramas.")