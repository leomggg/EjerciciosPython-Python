import json

with open("clientes.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

opcion = input("¿Qué quieres hacer?\nOpciones:\n1.Mostrar listado de clientes\n2.Introducir nuevo cliente\n3.Buscar cliente por email\n4.Guardar clientes premium\nOtro -> Salir\n ")

if opcion == '1': 
    for linea in datos:
        print(linea)

elif opcion == '2':
    datosValidos = True

    nombre = input("Introduce el nombre del nuevo cliente: ").lower()
    email = input("Introduce el email del nuevo cliente: ").lower()
    if '@' not in email: datosValidos = False
    ciudad = input("Introduce la ciudad del nuevo cliente: ").lower()
    telefono = input("Introduce el teléfono del nuevo cliente: ")
    if float(telefono) > 999999999 or float(telefono) < 100000000: datosValidos = False
    pedidos = input("Introduce la lista de pedidos del nuevo cliente (XX-XX-...): ")
    
    nuevo = {"nombre": nombre, "email": email, "ciudad": ciudad, "telefono": telefono, "pedidos": pedidos}
    
    if datosValidos == True:
        datos.append(nuevo)
        print("Cliente registrado")
    else: print("Datos incorrectos")

elif opcion == '3':
    email = input("Introduce el email del cliente: ").lower()
    encontrado = ""
    
    for line in datos:    
        if line["email"] == email:
            encontrado = line
            break

    if encontrado: print(encontrado)
    else: print("Correo no registrado")

elif opcion == '4':
    premium = []

    for line in datos:
        total = sum(map(float, line["pedidos"].split('-')))
        if total > 500:
            premium.append(line)
            print("Clientes premium añadidos a clientes_premium.txt")

    with open("clientes_premium.txt", "w", encoding="utf-8") as archivopremium:
        archivopremium.write(f"{premium}\n")

else: print("Saliendo del programa...")    


with open("clientes.json", "w", encoding="utf-8") as archivo:
    escritor = json.dump(datos, archivo, indent=5,ensure_ascii=False)