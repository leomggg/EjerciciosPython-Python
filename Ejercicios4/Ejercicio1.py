class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola {nombre}, tienes {edad} años y eres de {nacionalidad}") 


nombre = input("Por favor introduce tu nombre: ")
edad = input("Por favor introduce tu edad: ")
nacionalidad = input("Por favor introduce tu nacionalidad: ")

p1= Persona(nombre, edad, nacionalidad)
p1.saludar()