class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def hablar(self):
        print("Sonido genérico")

class Perro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)

    def hablar(self):
        print("Guau")

a1 = Animal("Animal1", "Especie1")
p1 = Perro("Toby", "Caniche")

a1.hablar()
p1.hablar()