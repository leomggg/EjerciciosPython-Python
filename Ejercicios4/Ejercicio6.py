class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
    
    def mostrar_info(self):
        print(f"Título del libro: {self.titulo},\n Autor: {self.autor},\n Año de publicación: {self.ano_publicacion}")

l1 = Libro("Karl Marx", "Manifiesto Comunista", 1833)
l1.mostrar_info()