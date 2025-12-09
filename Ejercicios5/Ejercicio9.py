class Calendario:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def fecha_completa(self):
        if(self.dia < 10): self.dia=f"0{self.dia}"
        if(self.mes < 10): self.mes=f"0{self.mes}"
        print(f"{self.dia}-{self.mes}-{self.ano}")

    def es_bisiesto(self):
      if(self.ano % 400 == 0): print("Es año bisiesto")
      elif(self.ano % 4 == 0 and self.ano % 100 != 0): print("Es año bisiesto")
      else: print("No es año bisiesto")

c1 = Calendario(10,5,2016)
c1.fecha_completa()
c1.es_bisiesto()