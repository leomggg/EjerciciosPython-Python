class Rectangulo:
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura

    def calcArea(self):
        area= self.base * self.altura
        print(f"El área del retángulo es: {area}")

base = int(input("Introduce la base del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))

r1 = Rectangulo(base, altura)
r1.calcArea()