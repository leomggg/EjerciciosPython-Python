class Telefono:
    def __init__(self, marca, modelo, tlf):
        self.marca = marca
        self.modelo = modelo
        self.tlf = tlf

    def hacer_llamada(self, tlf):
        print(f"Llamando a {tlf}")

    def enviar_mensaje(self, tlf):
        print(f"Enviando mensaje a {tlf}")
    
    def detalles(self):
        print(f"Marca del teléfono: {self.marca}\n Modelo: {self.modelo}\n Número de teléfono: {self.tlf}")

t1 = Telefono("Poco", "M6", "629321654")
t1.hacer_llamada(695874123)
t1.enviar_mensaje(159487623)
t1.detalles()