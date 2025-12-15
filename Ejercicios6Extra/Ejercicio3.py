import csv

buscar = input("Escribe el producto que quieres buscar: ")

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    next(lector)
    encontrado = False

    for fila in lector:
        if (fila[1] == buscar):
            print(f"El precio es: {fila[2]}")
            encontrado = True
            break
    
    if (encontrado == False): print("No se encuentra ese producto")