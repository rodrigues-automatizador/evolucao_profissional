import math

# Crie um programa que peça ao usuário para inserir um angulo
# em graus e calcule o seno, cosseno e tangente

angulo = int (input("Digite o valor do angulo: "))
radianos = math.radians(angulo)

seno = math.sin(radianos)

print(seno)

cosseno = math.cos(math.radians(angulo))
print(cosseno)

tangente = math.tan(math.radians(angulo))
print(tangente)