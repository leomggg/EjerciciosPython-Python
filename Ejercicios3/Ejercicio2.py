class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if(self.saldo >= cantidad):
            self.saldo -= cantidad 

    def imprimir(self):
        print(f"Saldo actual: {self.saldo}")

c1 = CuentaBancaria("Vin diesel", 3000)
c1.ingresar(300)
c1.imprimir()
c1.retirar(2500)
c1.imprimir()