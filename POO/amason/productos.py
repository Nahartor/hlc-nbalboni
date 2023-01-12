# PRODUCTOS PARA LA APP DE AMASON

# Creamos un producto genérico
class Producto:
    # Atributos de la clase

    # Constructor
    def __init__(self,nombre,codigo,precio,descripcion):
        # Atrbutos de instancia
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.descripcion = descripcion

# Creamos cada tipo de producto como una clase hija
class Libro(Producto):
    # Constructor de la clase hija
    def __init__(self, nombre, codigo, precio, descripcion,isbn,genero,autor,tapa):
        super().__init__(nombre, codigo, precio, descripcion)
        self.isbn = isbn