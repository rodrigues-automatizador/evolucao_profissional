# Crie um programa que peça ao usuário para digitar o raio de um circulo
# Em seguida, o programa deve calcular e mostrar a área e comprimento do círculo

import math

raio = int(input("Digite a área do circulo: "))
area = math.pi * raio ** 2

comprimento = 2 * math.pi * raio

print(f"A áreea do circulo é: {area}")
print(f"O comprimento do circulo é: {comprimento}")