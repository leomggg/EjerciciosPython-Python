class Empleado():
    def __init__(self, nombre, puesto, salario, antiguedad):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad
    
    def aumento_salario(self, porcentaje):
        self.salario += ((self.salario * porcentaje)/100)

    def mostrar_informacion(self):
        print(f"Nombre del empleado: {self.nombre}\n Puesto: {self.puesto}\n Salario: {self.salario}€\n Antigüedad: {self.antiguedad}")

e1 = Empleado("Manuel", "Técnico", 1000, 2)
e1.aumento_salario(30)
e1.mostrar_informacion()