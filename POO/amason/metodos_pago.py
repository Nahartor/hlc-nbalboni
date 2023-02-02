# METODOS DE PAGO PARA LA APP DE AMASON


# Creamos un objeto genérico
class Pago:
    # Atributos de clase

    # Constructor
    def __init__(self, importe, divisa = "€"):
        self.importe = importe
        self.divisa = divisa

    def __str__(self):
        return f"Importe: {self.importe}\nDivisa: {self.divisa}"

    # Creamos los metodos para este objeto
    def pagar(self,importe,divisa):
        opcion=input("La divisa por defecto es el euro(€). ¿Desea modificarla? (S/N): ")
        if opcion == "S":
            divisa=input("Introduzca nueva divisa: ")
        
        print(f"Realizando pago genérico por valor de {importe}{divisa}.")
        metodo_pago = input("Seleccione un método de pago: ")
        
        if metodo_pago == "Tarjeta":
            Tarjeta.pagar(self)
        elif metodo_pago == "Transferencia":
            Transferencia.pagar(self)
        elif metodo_pago == "Bizum":
            Bizum.pagar(self)
        else:
            PayPal.pagar(self)

# Creamos los diferentes objetos correspondientes a los métodos de pago que deseamos implementar

# Tarjeta
class Tarjeta(Pago):
    def __init__(self, saldo, titular, direccion_facturacion, num_tarjeta, caducidad_tarjeta, cvv):
        self.saldo = saldo
        self.titular = titular
        self.direccion_facturacion = direccion_facturacion
        self.num_tarjeta = num_tarjeta
        self.caducidad_tarjeta = caducidad_tarjeta
        self.cvv = cvv

    def __str__(self):
        return f"Saldo: {self.saldo}\nTitular: {self.titular}\nDirección de facturación: {self.direccion_facturacion}\nNúmero de tarjeta: {self.num_tarjeta}\nCaducidad: {self.caducidad_tarjeta}\nCVV: {self.cvv}"

    # Creamos los metodos para este objeto
    def pagar(self):
        var1=input("Seleccione la tarjeta con la que desea pagar: ")

        if var1=="Tarjeta1":
            print("Estas pagando con la Tarjeta1.")
            print("La información de la Tarjeta1 es la siguiente:")
            print(tarjeta1)

# Transferencia
class Transferencia(Pago):
    def __init__(self, importe, divisa, num_cuenta, concepto = "Compra AMASON"):
        super().__init__(importe, divisa)
        self.num_cuenta = num_cuenta
        self.concepto = concepto

    def __str__(self):
        return f"{super().__str__()}\nNúmero de cuenta: {self.num_cuenta}\nConcepto: {self.concepto}"

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando mediante transferencia.")

# Bizum
class Bizum(Pago):
    def __init__(self, importe, divisa, telefono, concepto = "Compra AMASON"):
        super().__init__(importe, divisa)
        self.telefono = telefono
        self.concepto = concepto

    def __str__(self):
        return f"{super().__str__()}\nTeléfono: {self.telefono}\nConcepto: {self.concepto}"

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando con Bizum.")

# PayPal
class PayPal(Pago):
    def __init__(self, importe, divisa, correo, contraseña):
        super().__init__(importe, divisa)
        self.correo = correo
        self.contraseña = contraseña

    def __str__(self):
        return f"{super().__str__()}\nCorreo: {self.correo}\nContraseña: {self.contraseña}"

    # Creamos los metodos para este objeto
    def pagar(self):
        print("Estas pagando con PayPal.")


# Cremos métodos de pago
tarjeta1=Tarjeta(200,"Nicolás Balboni","Mi Casa",1234123412341234,"05/26",122)
tarjeta2=Tarjeta(500,"Amparo Valladares Casero","La roza del caracol",4321432143214321,"11/12",211)
transferencia1=Transferencia("","","1111223333444455556666","")
transferencia2=Transferencia("","","2222334444555566667777","")
bizum1=Bizum("","",666123123,)