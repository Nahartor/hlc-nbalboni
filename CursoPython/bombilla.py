import random


estados = ("Encendida","Apagada")
estado=random.choice(estados)
print(estado)

class Bombilla:
    def _init_ (self, s=estado):
        self.status= s

    def encender(self):
        if estado == "Encendida":
            print("La bombilla ya estaba encendida")
        
        else:
            estado="Apagada"

    def apagar(self):
        if estado == "Apagada":
            print("La bombilla ya estaba apagada")
        
        else:
            estado="Encendida"


bombi1=Bombilla
opcion=input("¿Quieres ENCENDER/APAGAR la bombilla? e/a")

if opcion == "e":
    bombi1.encender()

elif opcion== "a":
    bombi1.apagar()
else:
    print("¡Hasta luego!")

print(estado)
