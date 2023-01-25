# CARRITO PARA LA APP DE AMASON

import metodos_pago

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
    def añadir_tarjeta():
        temporal=(input("Ingrese el titular: "),input("Ingrese la dirección de facturación: "),input("Ingrese el numero de tarjeta: "),input("Ingrese la fecha de caducidad: "),input("Ingrese el cvv: "))
        nombre_tarjeta="Tarjeta1"
        nombre_tarjeta=temporal