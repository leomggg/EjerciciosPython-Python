class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def disponibilidad(self):
        if(self.stock > 0): print(f"Existe disponibilidad: {self.stock}")
        else: print("No existe disponibilidad")

p1 = Producto("Patata", 30, 5)
p1.disponibilidad()