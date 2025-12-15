import shutil

shutil.copy("datos.txt", "copia.txt")

with open("copia.txt",  "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print(texto)