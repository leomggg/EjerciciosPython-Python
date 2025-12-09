class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Saldo actual: {self.saldo}")
    
    def retirar(self, cantidad):
        self.saldo -= cantidad
        print(f"Saldo actual: {self.saldo}")

c1 = CuentaBancaria("Jesús", 3000)
c1.depositar(100)
c1.retirar(500)