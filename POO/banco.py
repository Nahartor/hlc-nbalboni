# Insertamos el objeto
from tarjeta import Tarjeta
from credito import TarjetaCredito

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
tarjeta1.recargar(1000)

tarjeta_credito_1=TarjetaCredito("Santander","Manolito Gafotas","2356235623562356","11/25",422,500)
print(f"La tarjeta {tarjeta_credito_1.numero} tiene {tarjeta_credito_1.credito}€ de crédito.")

print(tarjeta1)