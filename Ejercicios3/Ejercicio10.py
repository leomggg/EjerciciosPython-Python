import json

amai = {
    "nombre": "rayo makuin",
    "edad": 90,
    "ciudad": "fondo de bikini"
}

cadenaJson = json.dumps(amai)
print(cadenaJson)

diccionarioNuevo = json.loads(cadenaJson)
print(diccionarioNuevo)