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

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, Descripción: {self.descripcion}"

# Creamos cada tipo de producto como una clase hija

# Libro
class Libro(Producto):
    # Constructor de la clase hija
    def __init__(self, nombre, codigo, precio, descripcion,isbn,genero,autor,tapa):
        super().__init__(nombre, codigo, precio, descripcion)
        self.isbn = isbn
        self.autor = autor
        self.genero = genero
        self.tapa = tapa

    def __str__(self):
        return f"{super().__str__()}, ISBN: {self.isbn} , Autor: {self.autor} , Género: {self.genero} , Tapa: {self.tapa}" 

# Videojuego
class Videojuego(Producto):
    # Constructor de la clase hija
    def __init__(self, nombre, codigo, precio, descripcion,plataforma,desarrolladora,genero,pegi):
        super().__init__(nombre, codigo, precio, descripcion)
        self.plataforma = plataforma
        self.desarrolladora = desarrolladora
        self.genero = genero
        self.pegi = pegi

    def __str__(self):
        return f"{super().__str__()}\nPlataforma: {self.plataforma}\nDesarrolladora: {self.desarrolladora}\nGénero: {self.genero}\nPEGI: {self.pegi}"

# Mueble
class Mueble(Producto):
    def __init__(self, nombre, codigo, precio, descripcion,dimensiones,tipo,material):
        super().__init__(nombre, codigo, precio, descripcion)
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"{super().__str__()}\nDimensiones: {self.dimensiones}\nTipo: {self.tipo}\nMaterial: {self.material}"

# Ropa
class Ropa(Producto):
    def __init__(self, nombre, codigo, precio, descripcion,talla,material,corte = "Unisex"):
        super().__init__(nombre, codigo, precio, descripcion)
        self.talla = talla
        self.material = material
        self.corte = corte

    def __str__(self):
        return f"{super().__str__()}\nTalla: {self.talla}\nMaterial: {self.material}\nCorte: {self.corte}"


