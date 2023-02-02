# CARRITO PARA LA APP DE AMASON

import metodos_pago
import productos

# Cliente
class Cliente:

    # Atributos de clase
    
    # Constructor
    def __init__(self,nombre,apellidos,nivel):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nivel = nivel

# Carrito
class Carrito:

    # Atributos de clase

    #Constructor
    def __init__(self,identificador,fecha,num_articulos,cliente):
        self.idetificador = identificador
        self.fecha = fecha
        self.num_articulos = num_articulos
        self.cliente = cliente

    # Métodos del carrito
    # Añadir articulo a la cesta
    #def añadir_articulo(nombre,cantidad)






# Creamos productos
libro1=productos.Libro("Harry Potter y la piedra filosofal",1234,23,"Primer libro de la saga de Harry Potter",
"HP123","Fantasia","J.K.Rowling","Dura")
videojuego1=productos.Videojuego("Rocket Leage",2345,30,"Futbol con coches","Epic Games","Psyonix","eSports",8)
mueble1=productos.Mueble("Skrunfel",3456,50,"Es una estantería...¿Qué más quieres saber?","60x70x25","Estantería","Madera")
ropa1=productos.Ropa("Camiseta",4567,20,"Se mete por la cabeza","XXL","Algodón","Hombre")



metodos_pago.Pago.pagar("",25,"Euros")