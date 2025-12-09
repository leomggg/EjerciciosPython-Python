class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def aumentar_salario(self, porcentaje):
        self.salario += ((porcentaje * self.salario) / 100)
        print(f"Nuevo salario: {self.salario}")

e1 = Empleado("Juan", "Técnico", 1000)
e1.aumentar_salario(30)