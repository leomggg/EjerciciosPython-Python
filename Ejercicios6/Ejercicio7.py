palabra = input("Escribe que palabra quieres buscar: ")

with open("texto.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    numveces = texto.count(palabra)

print(f"Aparece {numveces} vez/veces")