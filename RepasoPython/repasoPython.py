# Author: Nicolás Balboni
# Date: 12/01/2022
# Name: Repaso Python

# 1. Crear una lista vacía llamada lista_numeros
lista_numeros=[]

# 2. Añadir los números 2,5,6,7,9 a la lista anterior.
lista_nuevos=[2,5,6,7,9]
lista_numeros.extend(lista_nuevos)
print(lista_numeros)

# 3. Obtener el tamaño de la lista.
print(f"El tamaño de la lista es {len(lista_numeros)}")

# 4. Añadir la lista lista_2 =[3,4,8] a la lista anterior
lista_numeros.extend([3,4,8])
print(lista_numeros)

# 5. Modificar el elemento de la posición 4 por un 3.
lista_numeros[4]=3
print(lista_numeros)

# 6. Obtener los números que están en la posición 2,3,4 y 5
print(lista_numeros[2:6])
print(lista_numeros[2:7:2])
#Dar la vuelta a la lista
print(lista_numeros[::-1])

# 7. Convertir la lista en tupla.
lista_numeros=tuple(lista_numeros)
print(lista_numeros)
#lista_numeros.append(5) #No se puede modificar una tupla

#Convertir la tupla en lista.
lista_numeros=list(lista_numeros)
print(lista_numeros)

# 8. Crear una tupla con los valores 3,5,7,8
miTupla=(3,5,7,8)

# 9. Eliminar el elemento en la posición 2.
numero_elminado=lista_numeros.pop(2)
print(lista_numeros)

# 10. Comprobar si el número 7 está contenido en la tupla anterior.
numero=7
if numero in miTupla:
    print("Está")

else:
    print("No está")

# 11. Comprobar si el número 1 no está contenido en la tupla anterior.
numero=1
if numero not in miTupla:
    print("No está")

else:
    print("Está")

# 12. Obtener el número mayor de la lista_numeros.
print(f"El valor mayor es {max(lista_numeros)}")

# 13. Obtener el número menor de la lista_numeros sin utilizar funciones de Python.
# Forma 1. Ordenar la lista ascendentemente y tomar el primero.
lista_nuevos.sort()
menor1=lista_numeros[0]
print(f"El número menor es {menor1}")

# Forma 2. 
menor2=lista_numeros[0]
for numero in lista_numeros:
    if numero < menor2:
        menor2=numero
print(f"EL número menor es {menor2}")

# 14. Ordenar la lista de números de mayor a menor.
lista_ordenada=sorted(lista_numeros, reverse=True)
print(lista_ordenada)

# 15. Ordenar la lista de números de menor a mayor.
lista_ordenada=sorted(lista_numeros)
print(lista_ordenada)

# 16. Crear un diccionario con la siguiente información:
## a. Codigo: A54R
## b. Producto: Batidora
## c. Marca: Taurus
## d. Potencia: 1000W
## e. Precio: 20,50

producto={'codigo':'A543R', 'producto':'Batidora', 'marca':'Taurus', 'potencia':'1000W', 'precio':'20,50'}

print(producto)
print(producto['precio'])
print(producto.keys())
print(producto.values())

# 17. Añadir el diccionario anterior a una lista de productos que inicialmente está vacía.
productos=[]
productos.append(producto)
print(productos)

# 18. Añade otro producto más.
producto2={'codigo':'A544R', 'producto':'BatiCao', 'marca':'ColaCao', 'potencia':'1000W', 'precio':'Free'}
productos.append(producto2)

# 19. Elimina el producto con código A543R
for producto in productos:
    if producto['codigo'] == 'A543R':
        productos.remove(producto)

# 20. Imprime la lista de diccionarios por pantalla sin formatear.
print(productos)

# 21. Imprime el código de cada producto y su precio.
for producto in productos:
    print(producto['codigo'], producto['precio'])

# 22. Modifica el precio del producto con codigo A543R 25€.
for producto in productos:
    if producto['codigo'] == 'A544R':
        producto['precio']='15€'

print(productos)

# 23.
"""Escribe el siguiente if utilizando formato corto:
if edad>18:
	print(“Mayor de edad”)
else:
	print(“Menor de edad”)"""

edad=15
print("Mayor de edad") if edad>18 else print("Menor de edad")

# 25. A partir de la fecha 23/08/2022 extraiga el día, el mes y el año.
fecha="23/08/2022"
dia=fecha[0:fecha.find('/')]
print(dia)
mes_anyo=fecha[fecha.find('/')+1:]
print(mes_anyo)
mes=mes_anyo[0:mes_anyo.find('/')]
print(mes)
anyo=mes_anyo[mes_anyo.find('/')+1:]
print(anyo)

# Importar la librería calendar. Imprimir el calendario del mes actual.
import datetime
import calendar
x= datetime.datetime.now().year
y= datetime.datetime.now().month
print(calendar.month(x,y))