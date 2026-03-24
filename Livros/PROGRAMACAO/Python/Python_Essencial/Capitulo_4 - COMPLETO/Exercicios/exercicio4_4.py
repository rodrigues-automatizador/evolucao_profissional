import math

# crie um programa que peça ao usuário para inserir
# um número e calcule o logaritmo natural

base = int(input("Digite a base do logaritmo: "))
expoente = int(input("Digite o expoente do logaritmo: "))

resultado = math.log(expoente, base)

print(resultado)
