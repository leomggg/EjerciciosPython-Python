import datetime

ahora = datetime.datetime.now()
print("Fecha actual:", ahora.strftime("%d-%m-%Y %H:%M:%S"))

f1 = input("\nEscribe la primera fecha (dd-mm-yyyy): ")
f2 = input("Escribe la segunda fecha (dd-mm-yyyy): ")

fecha1 = datetime.datetime.strptime(f1, "%d-%m-%Y")
fecha2 = datetime.datetime.strptime(f2, "%d-%m-%Y")

resta = fecha2 - fecha1
print(f"Hay {resta.days} días de diferencia")