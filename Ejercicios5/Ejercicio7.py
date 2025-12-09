class Rectangle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.base * self.altura
        print(area)

    def perimetro(self):
        perimetro = 2*(self.base + self.altura)
        print(perimetro)
    
    def cuadrado(self):
        es_cuadrado = False
        if(self.base == self.altura): es_cuadrado = True
        print(f"¿Es un cuadrado? {es_cuadrado}")

c1 = Rectangle(20, 30)
c1.area()
c1.perimetro()
c1.cuadrado()