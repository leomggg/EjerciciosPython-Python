import json
from Empleado import Empleado

datos = [
    {"nombre": "Maria Lopez","puesto": "Gerente","salario": 2500,"antiguedad": 12,"ventas": []},
    {"nombre": "Carlos Ruiz","puesto": "Comercial","salario": 1100,"antiguedad": 3,"ventas": [500, 120, 300, 50]}
]

listaEmpleados = []

def guardar():
    with open("plantilla.json", "w", encoding="utf-8") as archivo:
        escritor = json.dump(datos, archivo, indent=5, ensure_ascii=False)

def cargar():
    with open("plantilla.json", "r", encoding="utf-8", newline="") as archivo:
        datos = json.load(archivo)

        for user in datos:
            nuevo = Empleado(user["nombre"], user["puesto"], user["salario"], user["antiguedad"], user["ventas"])
            listaEmpleados.append(nuevo)

cargar()

opcion = input("Elige una opcion:\n1.Listar empleados\n2.Fichar nuevo empleado\n3.Consultar nómina\n4.Exportar veteranos\nOtro -> Salir\n ")

if opcion == '1':
    for emp in listaEmpleados:
        print(emp.__str__())

elif opcion == '2':
    esValido = True

    nombre = input("Introduce el nombre del nuevo empleado: ")
    puesto = input("Introduce el puesto del nuevo empleado: ")
    salario = float(input("Introduce el salario del nuevo empleado: "))
    antiguedad = int(input("Introduce los años de antigüedad del nuevo empleado: "))
    #hay que pasar las ventas de string a [] -> json.loads()
    ventas = json.loads(input("Introduce la lista de ventas del nuevo empleado([XX, XX, XX]): "))

    if esValido == True:
        nuevo = Empleado(nombre, puesto, salario, antiguedad, ventas)
        listaEmpleados.append(nuevo)
        nuevo = {"nombre": nombre,"puesto": puesto,"salario": salario,"antiguedad": antiguedad,"ventas": ventas}
        datos.append(nuevo)
        guardar()
        print("Empleado guardado")
    else: print("Datos inválidos")

elif opcion == '3':
    usuario = input("Introduce el nombre del empleado a buscar: ")
    
    for emp in listaEmpleados:
        if emp.nombre == usuario:
            sueldo = emp.salario + emp.calcular_comision()
            print(f"El sueldo neto del empleado es: {sueldo}")

elif opcion == '4':
    with open("veteranos.txt", "w", encoding="utf-8") as veteranostexto:
        
        # se puede hacer de las dos formas
        for emp in listaEmpleados:
            if emp.antiguedad > 10: veteranostexto.write(f"Nombre: {emp.nombre} - Puesto: {emp.puesto}")

        # cargar()
        # for line in datos:
        #     if line["antiguedad"] > 10: veteranostexto.write(f"{line}")
        
    print("Veteranos filtrados en veteranos.txt")

else: print("Cerrando programa")    