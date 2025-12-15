import csv

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    
    for linea in lector:
        print(linea)