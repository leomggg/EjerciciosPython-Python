with open("datos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea adicional")
    
with open("datos.txt", "r", encoding="utf-8") as archivo2:
    leerarchivo = archivo2.read()

print(leerarchivo)