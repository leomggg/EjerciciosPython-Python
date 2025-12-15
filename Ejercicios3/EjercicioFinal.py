import json

#clases y heredar
class Empleado:
    def __init__(self, nombre, edad, departamento):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento

    def mostrarInfo(self):
        print(f"Empleado {self.nombre}, tiene {self.edad} años y trabaja en el departamento de {self.departamento}")

class Gerente(Empleado):
    def __init__(self, nombre, edad, departamento, equipo):
        super().__init__(nombre, edad, departamento)
        self.equipo = equipo

    def mostrarInfo(self):
        print(f"Gerente {self.nombre}, tiene {self.edad} años y trabaja en el departamento de {self.departamento}, en el equipo {self.equipo}")

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, departamento, lenguaje):
        super().__init__(nombre, edad, departamento)
        self.lenguaje = lenguaje

    def mostrarInfo(self):
        print(f"Desarrollador {self.nombre}, tiene {self.edad} años y trabaja en el departamento de {self.departamento}, usa el lenguaje de {self.lenguaje}")

#creacion y lectura del json
datos = [
    {"tipo": "Gerente", "nombre": "Ana García", "edad": 45, "departamento": "Ventas", "equipo": 12},
    {"tipo": "Desarrollador", "nombre": "Carlos Pérez", "edad": 29, "departamento": "Tecnología", "lenguaje": "Python"},
    {"tipo": "Empleado", "nombre": "Lucía Méndez", "edad": 34, "departamento": "Recursos Humanos"},
    {"tipo": "Desarrollador", "nombre": "Javier Ruiz", "edad": 25, "departamento": "Tecnología", "lenguaje": "Java"},
    {"tipo": "Gerente", "nombre": "Roberto Díaz", "edad": 50, "departamento": "Operaciones", "equipo": 25}
]

with open("registro.json", "w+", encoding="utf-8") as archivo:
    escritor = json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
empleados = []
try:
    with open("registro.json", "r", encoding="utf-8") as archivo:
        lector = json.load(archivo)

    for user in lector:
        tipo = user["tipo"]
        nombre = user["nombre"]
        edad = user["edad"]
        departamento = user["departamento"]

        if tipo == "Gerente":
            nuevo = Gerente(nombre, edad, departamento, user["equipo"])
        elif tipo == "Desarrollador":
            nuevo = Desarrollador(nombre, edad, departamento, user["lenguaje"])
        else: nuevo = Empleado(nombre, edad, departamento)

        empleados.append(nuevo)
        nuevo.mostrarInfo()
except FileNotFoundError:
    print("El archivo no existe")