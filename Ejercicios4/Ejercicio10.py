class Calendario:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def fecha_completa(self):
        if (self.dia < 10): self.dia= f"0{self.dia}"
        if (self.mes < 10): self.mes= f"0{self.mes}"
        print(f"{self.dia}-{self.mes}-{self.ano}")

c1 = Calendario(1, 12, 1899)
c1.fecha_completa()