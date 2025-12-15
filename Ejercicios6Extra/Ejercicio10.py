import json
import csv

with open("datos.json", "r", encoding="utf-8") as archivo:
    lectorjson = json.load(archivo)


with open("datos_convertidos.csv", "w", encoding="utf-8") as archivo2:
    encabezado = ["nombre", "edad", "ciudad"]

    diccsv = csv.DictWriter(archivo2, fieldnames=encabezado)

    diccsv.writeheader

    for elem in lectorjson:
        diccsv.writerow(elem)
