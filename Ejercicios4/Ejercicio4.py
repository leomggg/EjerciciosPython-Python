class Estudiante:
    def __init__(self, nombre, curso, nota_final):
        self.nombre = nombre
        self.curso = curso
        self.nota_final = nota_final
    
    def aprobar(self):
        if (self.nota_final <5): print(f"Suspenso")
        else: print("Aprobado")

e1 = Estudiante("Manuel", "1ºDAM", 7)
e1.aprobar()