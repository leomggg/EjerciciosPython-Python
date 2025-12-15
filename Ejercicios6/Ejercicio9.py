import csv

with open("usuarios.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    
    escritor.writerow(["Nombre", "Edad"])
    escritor.writerow(["Ana", 25])
    escritor.writerow(["Luis", 30])
    escritor.writerow(["María", 28])

with open("usuarios.csv", "r") as archivo:
    lector = csv.reader(archivo)
    
    for fila in lector:
        print(f"{fila[0]}, {fila[1]}")