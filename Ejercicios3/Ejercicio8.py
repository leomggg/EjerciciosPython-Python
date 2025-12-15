import random

numero = random.randint(0, 6)
print("Tirando el dado...")
print(f"El dado ha salido: {numero}")

listanum = []

for i in range(10):
    numero = random.randint(1, 100)
    listanum.append(numero)

listanum.sort(reverse=True)

print(f"Lista de 10 números random(ordenada): {listanum}")