class CuentaBancaria:
    def __init__(self, titular, saldo, tipo_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
    
    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if (cantidad <= self.saldo): self.saldo -= cantidad
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def tipo_de_cuenta(self):
        print(f"Tipo de cuenta: {self.tipo_cuenta}")

c1 = CuentaBancaria("José", 3000, "Tipo 1")
c1.depositar(300)
c1.mostrar_saldo()
c1.tipo_de_cuenta()
c1.retirar(3200)
c1.mostrar_saldo()