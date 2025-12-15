import csv

with open("estudiantes.csv", "w", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    encabezado = (["Nombre", "Edad", "Curso"])

    escritor.writerow(encabezado)
    escritor.writerow(["Ana", 20, "Matemáticas"])
    escritor.writerow(["Pedro", 22, "Física"])
    escritor.writerow(["María", 21, "Química"])

    