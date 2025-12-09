class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def encender(self):
        print(f"El coche está encendido")
    
    def apagar(self):
        print(f"El coche está apagado")

c1 = Coche("Ford", "Focus", "Rojo")
c1.encender()
c1.apagar()