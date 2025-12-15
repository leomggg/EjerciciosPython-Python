import json

brrr = input("Escribe el título de una nueva tarea: ")

with open("tareas.json", "r", encoding="utf-8") as archivo:
    anuelaa = json.load(archivo)

anuelaa["tareas"].append(brrr)

with open("tareas.json", "w", encoding="utf-8") as archivo:
    bebesitaaa = json.dump(anuelaa, archivo, indent=1, ensure_ascii=False)