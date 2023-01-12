from tarjeta import Tarjeta

# Vamos a crear la clase TarjetaCredito que hereda de Tarjeta
class TarjetaCredito(Tarjeta):
    # Constructor de la clase hija
    def __init__(self,entidad,titular,numero,caducidad,cvv,credito):
        super().__init__(entidad,titular,numero,caducidad,cvv)
        self.credito = credito

    def pagar(self,cantidad):
        # Sobre escribimos el método pagar, ya que no es lo mismo pagar a crédito que pagar a débito
        pass

    