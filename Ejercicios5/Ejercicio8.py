class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def hacerSonido(self):
        print("Sonido genérico")
    
class Perro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)
    
    def hacerSonido(self):
        print("Guau")

class Gato(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)

    def hacerSonido(self):
        print("Miau")

p1 = Perro("Toby", "Caniche")
g1 = Gato("Michi", "Naranja")
p1.hacerSonido()
g1.hacerSonido()