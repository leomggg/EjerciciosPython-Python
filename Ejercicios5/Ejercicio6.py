class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def reducir_stock(self, cantidad):
        if(cantidad <= self.stock): self.stock -= cantidad
    
    def actualizarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def disponibilidad(self):
        if(self.stock > 0): print(f"Hay disponibilidad: {self.stock}")
        else: print(f"No hay existencias")

p1 = Producto("Patatas", 10, 5)
p1.reducir_stock(1)
p1.actualizarPrecio(15)