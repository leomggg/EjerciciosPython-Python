class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def informacion(self):
        print(f"El vehículo es de la marca {self.marca}, modelo {self.modelo} y es de color {self.color}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, numPuertas):
        super().__init__(marca, modelo, color)
        self.numPuertas = numPuertas

    def informacion(self):
        print(f"El coche es de la marca {self.marca}, modelo {self.modelo}, es de color {self.color} y el número de puertas es de {self.numPuertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, numRuedas):
        super().__init__(marca, modelo, color)
        self.numRuedas = numRuedas

    def informacion(self):
        print(f"La moto es de la marca {self.marca}, modelo {self.modelo}, es de color {self.color} y el número de ruedas es de {self.numRuedas}")

c1 = Coche("Citroen", "C3", "Rojo", 4)
c1.informacion()
m1 = Moto("Yamaha", "Jogg R", "Negro", 2)
m1.informacion()