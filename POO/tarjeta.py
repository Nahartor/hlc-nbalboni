# PLANTILLA PARA CREAR OBJETOS

class Tarjeta:
    # Atributos de clase

    # Constructor
    def __init__(self,entidad,titular,numero,caducidad,cvv):
        # Atributos de instancia (del objeto)
        self.entidad = entidad
        self.titular = titular
        self.numero = numero
        self.caducidad = caducidad
        self.cvv = cvv
        self.activa = False
        self.saldo = 0

    def __str__(self):
        return f"Entidad: {self.entidad}\nTitular: {self.titular}\nNúmero: {self.numero}"

    # Métodos --> COMPORTAMIENTO DE LOS OBJETOS
    def activar(self):
        if self.activa:
            print(f"La tarjeta con número {self.numero} ya está activa.")
        else:
            self.activa = True
            print(f"Activando la tarjeta con número {self.numero}...")

    def pagar(self,cantidad):
        if self.activa:
            print(f"Pagando {cantidad}€ con la tarjeta {self.numero}...")
        else:
            print(f"ERROR: La tarjeta {self.numero} no esta activa.")

    def anular(self):
        if not self.activa:
            print(f"La tarjeta con número {self.numero} ya está desactivada.")
        else:
            self.activa = False
            print(f"Desactivando la tarjeta con número {self.numero}...")

    def recargar(self,importe):
        print(f"El saldo actual de la tarjeta {self.numero} es de:  {self.saldo}.")
        self.saldo+=importe
        print(f"Recagando {importe}€ en la tarjeta {self.numero}...")
        print(f"El nuevo saldo para la tarjeta {self.numero} es de: {self.saldo}.")

# Instanciar una clase --> Crear un objeto
tarjeta1=Tarjeta("ING","Nicola Balboni","1234123412341234","12/24",123)
tarjeta2=Tarjeta("BBVA","Franccesco Bergolinni","4321432143214321","01/25",321)

print(type(tarjeta1))

# COn el objeto seguido de punto accdenemos al contenido del ojbeto, atributos y métodos
tarjeta1.activar() # Invocar un método del objeto tarjeta1
print(tarjeta1.titular)
tarjeta2.activar()
print(tarjeta2.titular)
tarjeta1.pagar(50)
tarjeta1.anular()
tarjeta1.pagar(20)