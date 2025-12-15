import json

nombre = input("Escribe el nombre de una persona: ")
edad = input("Escribe la edad de una persona: ")
ciudad = input("Escribe la ciudad de una persona: ")

datos = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

with open("usuario.json", "w", encoding="utf-8") as archivo:
    nengoflow = json.dump(datos, archivo, indent=3, ensure_ascii=False)

