# METODOS DE PAGO PARA LA APP DE AMASON

# Creamos un objeto genérico
class Pago:
    # Atributos de clase

    # Constructor
    def __init__(self, importe, divisa = "€"):
        self.importe = importe
        self.divisa = divisa

    # Creamos los metodos para este objeto
    def pagar(self,importe,divisa):
        print(f"Realizando pago genérico por valor de {importe}{divisa}.")
        metodo_pago = input("Seleccione un método de pago: ")
        
        if metodo_pago == "Tarjeta":
            Tarjeta.pagar()
        elif metodo_pago == "Transferencia":
            Transferencia.pagar("Transferencia1")
        elif metodo_pago == "Bizum":
            Bizum.pagar("Bizum1")
        else:
            PayPal.pagar("PayPal1")

# Creamos los diferentes objetos correspondientes a los métodos de pago que deseamos implementar

# Tarjeta
class Tarjeta(Pago):
    def __init__(self, titular, direccion_facturacion, num_tarjeta, caducidad_tarjeta, cvv):
        #super().__init__(importe, divisa)
        self.titular = titular
        self.direccion_facturacion = direccion_facturacion
        self.num_tarjeta = num_tarjeta
        self.caducidad_tarjeta = caducidad_tarjeta
        self.cvv = cvv

    # Creamos los metodos para este objeto
    def pagar():
        print("Estas pagando con tarjeta.")

# Transferencia
class Transferencia(Pago):
    def __init__(self, importe, divisa, num_cuenta, concepto = "Compra AMASON"):
        super().__init__(importe, divisa)
        self.num_cuenta = num_cuenta
        self.concepto = concepto

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando mediante transferencia.")

# Bizum
class Bizum(Pago):
    def __init__(self, importe, divisa, telefono, concepto = "Compra AMASON"):
        super().__init__(importe, divisa)
        self.telefono = telefono
        self.concepto = concepto

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando con Bizum.")

# PayPal
class PayPal(Pago):
    def __init__(self, importe, divisa, correo, contraseña):
        super().__init__(importe, divisa)
        self.correo = correo
        self.contraseña = contraseña

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando con PayPal.")

Pago.pagar("Pago1",100,"$")