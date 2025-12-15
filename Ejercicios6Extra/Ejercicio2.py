import csv

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    next(lector) #para saltar al siguiente y saltar el encabezado

    cont = 0

    for fila in lector:
        cont = cont + 1

print(f"Total de filas: {cont}")