import json
import csv

listaconvertir = []

with open("estudiantes.csv", "r", encoding="utf-8") as archivo:
    yets = csv.reader(archivo)

    next(yets)

    for fila in yets:
        if len(fila) == 0:
            continue

        nombre = fila[0]
        edad = fila[1]
        ciudad = fila[2]

        datos = {
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }

        listaconvertir.append(datos)

with open("datos.json", "w", encoding="utf-8") as archivo2:
    json.dump(listaconvertir, archivo2, indent=3, ensure_ascii=False)
