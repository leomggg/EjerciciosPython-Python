import json

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

    print(datos)