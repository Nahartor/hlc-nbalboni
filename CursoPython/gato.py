class Gato:
  """Esta clase define las características y el comportamiento de los gatos"""

  def __init__ (self, c = "pardo", r = "mestizo", s = "hembra", e = 1, p = 1.5): #_init_ se utiliza para inicializar el objeto. Aqui se define a si mismo y sus atributos.
    """Constructor con parámetros por defecto.""" #Se asigna un alias a cadad atrinuto (parámetro)
    self.color = c
    self.raza = r
    self.sexo = s
    self.edad = e
    self.peso = p
  
  #A partir de esta linea se van a definir diferentes métodos
  def maulla(self):
    print("Miauuuu")
 
  def ronronea(self):
    print("mrrrrrr");
    
  def come(self, comida):
    """A los gatos les gusta el pescado, si le damos otra comida, la rechazará."""
    if comida == "pescado":
      print("Hmmmm, gracias")
    else:
      print("Lo siento, yo solo como pescado")

  def pelea_con(self, contrincante):
    """
    Pone a pelear dos gatos.
    Solo se van a pelear dos machos entre sí.
    """
    if self.sexo == "hembra":
      print("no me gusta pelear")
    else:
      if contrincante.sexo == "hembra":
        print("no peleo contra gatitas")
      else:
        print("ven aquí que te vas a enterar")


#Definimos una instancia de nuestro objeto
garfield = Gato(s = "macho")

print("hola gatito")
garfield.maulla()

print("toma tarta")
garfield.come("tarta selva negra")
print("toma pescado, a ver si esto te gusta")
garfield.come("pescado")

tom = Gato(s = "macho", p = 2.5)

print("Tom, toma sopita de verduras")
tom.come("sopa de verduras")

lisa = Gato("blanco", "angora", "hembra", 3, 1.75)

print("gatitos, a ver cómo maulláis")
garfield.maulla()
tom.maulla()
lisa.maulla()

garfield.pelea_con(lisa)
lisa.pelea_con(tom)
tom.pelea_con(garfield)