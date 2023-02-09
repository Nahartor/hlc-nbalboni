# Author: Nicolás Balboni
# Date: 11/7/2022
# Name: Variables

# Definimos una variable GLOBAL
from curses import echo


x=0
print(x)

# Creamos una función
def funcion1(x):
    print(x)

    y=2
    print(y)
    x=x+1
    print(x)
    if x >= y:
        z=x-y
        print(z)

    else:
        z=y-x
        print(z)

    return z

numero=funcion1(1)