import json

class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, nueva):
        self.__marca = nueva
    
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, nueva):
        self.__modelo = nueva

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, nueva):
        if nueva < 1950: print("Error, año no válido")
        else: self.__ano = nueva

    def describir(self):
        print(f"Vehículo marca {self.marca}, modelo {self.modelo}, del año {self.ano}")
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, ano, numPuertas):
        super().__init__(marca, modelo, ano)
        self.__numPuertas = numPuertas

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, nueva):
        self.__marca = nueva
    
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, nueva):
        self.__modelo = nueva

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, nueva):
        if nueva < 1950: print("Error, año no válido")
        else: self.__ano = nueva

    @property
    def numPuertas(self):
        return self.__numPuertas
    @numPuertas.setter
    def numPuertas(self, nueva):
        if (nueva < 3 or nueva > 5): print("Error, número de puertas no válido")
        self.__numPuertas = nueva

    def describir(self):
        print(f"Coche marca {self.marca}, modelo {self.modelo}, del año {self.ano} con {self.numPuertas} puertas")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, cilindraje):
        super().__init__(marca, modelo, ano)
        self.__cilindraje = cilindraje

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, nueva):
        self.__marca = nueva
    
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, nueva):
        self.__modelo = nueva

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, nueva):
        if nueva < 1950: print("Error, año no válido")
        else: self.__ano = nueva

    @property
    def cilindraje(self):
        return self.__cilindraje
    @cilindraje.setter
    def cilindraje(self, nueva):
        if (nueva < 49 or nueva > 2500): print("Error, cilindrada no válida")
        else:self.__cilindraje = nueva

    def describir(self):
        print(f"Moto marca {self.marca}, modelo {self.modelo}, del año {self.ano} con {self.cilindraje} cc")

with open("vehiculos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

valoresValidos = True

try: 
    agregarTipo = input("Introduce el tipo de vehículo: ")
    agregarMarca = input("Introduce la marca de vehículo: ")
    agregarModelo = input("Introduce el modelo de vehículo: ")
    agregarAno = int(input("Introduce el año de vehículo: "))
    if agregarAno <= 1950:
        print("Año incorrecto") 
        valoresValidos = False       
    if agregarTipo == "auto":
        agregarExtra = int(input("Introduce el número de puertas de vehículo: "))
        if agregarExtra <0:
            print("Valores incorrectos")
            valoresValidos = False
    elif agregarTipo == "motocicleta": 
        agregarExtra = int(input("Introduce el cilindraje: "))
        if agregarExtra <0:
            print("Valores incorrectos")
            valoresValidos = False
    else: 
        print("Tipo de vehículo incorrecto")
        valoresValidos = False
    
    if valoresValidos == True:
        if agregarTipo == "auto":
            nuevo = {"tipo": "auto", "marca": agregarMarca, "modelo": agregarModelo, "ano": agregarAno, "numPuertas": agregarExtra}
        elif agregarTipo == "motocicleta":
            nuevo = {"tipo": "motocicleta", "marca": agregarMarca, "modelo": agregarModelo, "ano": agregarAno, "cilindraje": agregarExtra}
        datos.append(nuevo)
        print("Vehículo añadido")

    with open("vehiculos.json", "w", encoding="utf-8") as archivo:
        escritor = json.dump(datos, archivo, indent=5 ,ensure_ascii=False)

    #comprobacion
    print(datos)

#en futuras ejecuciones crear un vehiculo por cada elemento del json

except FileNotFoundError:
    print("Archivo .json no encontrado")