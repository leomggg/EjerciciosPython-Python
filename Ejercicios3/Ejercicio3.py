class CuentaBancaria:
    def __init__(self, titular, __saldo):
        self.titular = titular
        self.__saldo = __saldo
    
    def ingresar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if(self.__saldo >= cantidad):
            self.__saldo -= cantidad 

    def imprimir(self):
        print(f"Saldo actual: {self.__saldo}")

    def mostrarSaldo(self):
        print(self.__saldo)

c1 = CuentaBancaria("Vin diesel", 3000)
c1.ingresar(300)
c1.imprimir()
c1.retirar(2500)
c1.imprimir()
print(c1.titular)
print(c1.__saldo)