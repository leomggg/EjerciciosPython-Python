
import math


radio = float(input('Introduce el radio del círculo: '))

perimetro = 2 * math.pi * radio
area = math.pi * (radio * radio)

print(f'Perímetro del círculo: {perimetro}')

print(f'Área del círculo: {area}')