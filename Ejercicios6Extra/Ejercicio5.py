import csv

nombre = input("Escribe el nombre del alumno: ")
edad = input("Escribe la edad del alumno: ")
curso = input("Escribe el curso del alumno: ")

with open("estudiantes.csv", "a", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow([nombre, edad, curso])