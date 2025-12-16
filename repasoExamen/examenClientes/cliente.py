class Cliente:
    def __init__(self, nombre, email, ciudad, telefono, pedidos):
        self.__nombre = nombre
        self.__email = email
        self.__ciudad = ciudad
        self.__telefono = telefono
        self.__pedidos = pedidos
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, nuevo):
        if '@' not in nuevo: print("Correo inválido")
        else: self.__email = nuevo
    
    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, nuevo):
        self.__ciudad = nuevo
    
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, nuevo):
        if (nuevo < 100000000 or nuevo > 999999999): print("Número de teléfono inválido")
        else: self.__telefono = nuevo
    
    @property
    def pedidos(self):
        return self.__pedidos
    @pedidos.setter
    def pedidos(self, nuevo):
        self.__pedidos = nuevo
    
    def __str__(self):
        print(f"{self.nombre} - {self.email} - {self.ciudad} - {self.telefono} - {self.pedidos}")

    def ordenar(self):
        ordenado = list(map(int, self.pedidos.split('-')))
        return sorted(ordenado, reverse=True)
