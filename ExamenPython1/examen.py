# Author: Nicolás Balboni
# Date: 11/24/2022
# Name: Examen Python. Ejercicio 1

import random

#Generamos un resultado aleatorio para cada número del boleto

boleto_ganador = {1:[random.randint(1,49)],2:[random.randint(1,49)],3:[random.randint(1,49)],4:[random.randint(1,49)],5:[random.randint(1,49)],6:[random.randint(1,49)]}
#boleto_ganador={1:[49],2:[22],3:[33],4:[44],5:[25],6:[1]}
print(boleto_ganador) #Para controlar lo que hay en la variable boleto_ganador
#print(boleto_ganador[1][0])

#A continuación, pedimos los seis números al usuario

print("*****************LOTERÍAS DEL ESTADO*********************")
print("Intenta adivinar la combinación ganadora.")
print("Para ello debes introducir seis números entre 1 y 49.")
print("¡Que la suerte te acompañe!")
print("___________________________________________________________")
num1_usu=int(input("Introduce el primer número: "))
num2_usu=int(input("Introduce el segundo número: "))
num3_usu=int(input("Introduce el tercer número: "))
num4_usu=int(input("Introduce el cuarto número: "))
num5_usu=int(input("Introduce el quinto número: "))
num6_usu=int(input("Introduce el sexto número: "))

#Paso los números a una lista para poder mostrarlos facilmente por pantalla en su conjunto (no se volvera a usar)
combi_usuario=[]
combi_usuario.append(num1_usu)
combi_usuario.append(num2_usu)
combi_usuario.append(num3_usu)
combi_usuario.append(num4_usu)
combi_usuario.append(num5_usu)
combi_usuario.append(num6_usu)
print("___________________________________________________________")
print(f"Tu combinación es: {combi_usuario[0]}, {combi_usuario[1]}, {combi_usuario[2]}, {combi_usuario[3]}, {combi_usuario[4]}, {combi_usuario[5]}")
print("___________________________________________________________")

#Ahora pasamos a evaluar cada número por separado para saber si la combinación es correcta
if num1_usu==boleto_ganador[1][0] and num2_usu==boleto_ganador[2][0] and num3_usu==boleto_ganador[3][0] and num4_usu==boleto_ganador[4][0] and num5_usu==boleto_ganador[5][0] and num6_usu==boleto_ganador[6][0]:
    print("¡ENHORABUENA! Has acertado todos los números de la lotería.")
    print("___________________________________________________________")
    
if num1_usu==boleto_ganador[1][0]:
    print(f"Has acertado el primer número: {boleto_ganador[1][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu primer número es: {num1_usu}")
    print(f"El número correcto es: {boleto_ganador[1][0]}")
    print(f"Has fallado el primer número =(")
    print("___________________________________________________________")

if num2_usu==boleto_ganador[2][0]:
    print(f"Has acertado el segundo número: {boleto_ganador[2][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu segundo número es: {num2_usu}")
    print(f"El número correcto es: {boleto_ganador[2][0]}")
    print(f"Has fallado el segundo número =(")
    print("___________________________________________________________")

if num3_usu==boleto_ganador[3][0]:
    print(f"Has acertado el tercer número: {boleto_ganador[3][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu tercer número es: {num3_usu}")
    print(f"El número correcto es: {boleto_ganador[3][0]}")
    print(f"Has fallado el tercer número =(")
    print("___________________________________________________________")

if num4_usu==boleto_ganador[4][0]:
    print(f"Has acertado el cuarto número: {boleto_ganador[4][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu cuarto número es: {num4_usu}")
    print(f"El número correcto es: {boleto_ganador[4][0]}")
    print(f"Has fallado el cuarto número =(")
    print("___________________________________________________________")

if num5_usu==boleto_ganador[5][0]:
    print(f"Has acertado el quinto número: {boleto_ganador[5][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu quinto número es: {num5_usu}")
    print(f"El número correcto es: {boleto_ganador[5][0]}")
    print(f"Has fallado el quinto número =(")
    print("___________________________________________________________")

if num6_usu==boleto_ganador[6][0]:
    print(f"Has acertado el sexto número: {boleto_ganador[6][0]}")
    print("___________________________________________________________")

else:
    print(f"Tu sexto número es: {num6_usu}")
    print(f"El número correcto es: {boleto_ganador[6][0]}")
    print(f"Has fallado el sexto número =(")
    print("___________________________________________________________")


# Author: Nicolás Balboni
# Date: 11/24/2022
# Name: Examen Python. Ejercicio 2
    
#Cabecera
print("*****************************EJERCICIO 2******************************")
print("______________________________________________________________________")

import csv
archivo="/home/nbalboni/github/hlc-nbalboni/ExamenPython1/peliculas.csv"
peliculas=[]

#Cargamos las peliculas a una lista de diccionario
try:
    with open(archivo, 'r') as File:
        reader = csv.DictReader(File)
        for row in reader:
            peliculas.append(row)

except FileNotFoundError:
    print(f"El archivo {archivo} no existe, no se han podido cargar los nombres.")
except:
    print("Se ha producido un error inesperado.")
else:
    for i in range(5):#Lo de range(5) falla en el momento en el que añadamos un nuevo registro, pero no se como hacerlo de otra forma
        print(f"Titulo: {peliculas[i]['titulo']} - Director: {peliculas[i]['director']} - Año: {peliculas[i]['anyo']} - Género: {peliculas[i]['genero']}")

       
# Author: Nicolás Balboni
# Date: 11/24/2022
# Name: Examen Python. Ejercicio 2

#Cabecera
print("*****************************EJERCICIO 3******************************")
print("______________________________________________________________________")

def nueva_pelicula(peliculas):
    nueva_peli=[]
    titulo=input("Título: ")
    director=input("Director: ")
    genero=input("Género: ")
    anyo=input("Año: ")

    nueva_peli.append(titulo)
    nueva_peli.append(anyo)
    nueva_peli.append(genero)
    nueva_peli.append(director)

    print(f"Los datos de la película son: {nueva_peli}")
    peliculas['titulo']=titulo
    peliculas['director']=director
    peliculas['genero']=genero
    peliculas['anyo']=anyo

    #Ahora los guardamos como una nueva linea en el archivo csv
    with open(archivo, 'w'):
        csv.DictWriter(peliculas)

    return nueva_peli

nueva_pelicula(peliculas)