class Libro:
    def __init__(self, titulo, autor, ano_publicacion, precio):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.precio = precio
    
    def descuento(self, porcentaje):
        self.precio -= ((porcentaje * self.precio) / 100)
        print(f"Nuevo precio tras descuento: {self.precio}")

    def informacion(self):
        print(f"Título: {self.titulo}\n Autor: {self.autor}\n Año de publicación: {self.ano_publicacion}\n Precio: {self.precio} céntimos")
    
l1 = Libro("Karl Marx", "Manifiesto comunista", 1833, 8.99)
l1.descuento(30)
l1.informacion()