class Coche:
    def __init__(self, marca, modelo, color, km):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.km = km
    
    def conducir(self, km):
        self.km += km
    
    def detalles(self):
        print(f"Marca del coche: {self.marca}\n Modelo: {self.modelo}\n Color: {self.color}\n Kilometraje: {self.km}Km")

c1 = Coche("Seat", "Leon", "Amarillo", 300000)
c1.conducir(10000)
c1.detalles()