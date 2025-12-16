class Empleado:
    def __init__(self, nombre, puesto, salario, antiguedad, ventas):
        self.nombre = nombre
        self.__puesto = puesto
        self.__salario = salario
        self.antiguedad = antiguedad
        self.ventas = ventas

    @property
    def puesto(self):
        return self.__puesto
    @puesto.setter
    def puesto(self, nuevo):
        self.__puesto = nuevo

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, nuevo):
        if nuevo > 1150: self.__salario = nuevo 

    #[100, 200, 50]    
    def totalventas(self):
        return sum(self.ventas)

    def __str__(self):
        return f"Nombre: {self.nombre}\nPuesto: {self.puesto}\nsalario base: {self.salario}\nTotal ventas: {self.totalventas()}\n"

    def calcular_comision(self):
        if self.antiguedad > 2: return (self.totalventas() * 0.1)
        else: return (self.totalventas() * 0.05)