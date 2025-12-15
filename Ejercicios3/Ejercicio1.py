class Libro:
    def __init__(self, titulo, autor, ano_publi):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
    
    def imprimirDesc(self, descripcion):
        print(f"{self.titulo}: Este libro trata de {descripcion}")

libro1 = Libro("Manifiesto Comunista", "Karl Marx", "1833")
libro2 = Libro("Metamorfosis", "Franz Kafka", "1955")

libro1.imprimirDesc("todo lo que está bien en la vida")
libro2.imprimirDesc("un gaxo que se convierte en bixo y se ralla pila")