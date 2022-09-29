def contar_letras(texto):
    contador=0
    for letra in texto:
        contador+=1
    print(F"La cadena tiene {contador} letras.")

contar_letras("HOLA")
contar_letras("MAMAWEVASO")