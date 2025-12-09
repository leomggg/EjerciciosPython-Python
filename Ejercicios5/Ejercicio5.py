class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3)/3
        return promedio

    def aprobado(self):
        aprobado = True
        if (self.calcular_promedio() >= 6): return aprobado
        else:
            aprobado = False
            return aprobado
    
    def informacion(self):
        print(f"Nombre del estudiante: {self.nombre}\n ¿Aprobado? {self.aprobado()}")

e1 = Estudiante("José", 10, 5, 0)
e1.informacion()