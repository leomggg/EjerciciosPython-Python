#Con el código del ejercicio 2
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print("Error inesperado")

