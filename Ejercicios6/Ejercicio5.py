with open("texto.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    numpalabra = len(texto.split())
    
print(numpalabra)
print(texto)