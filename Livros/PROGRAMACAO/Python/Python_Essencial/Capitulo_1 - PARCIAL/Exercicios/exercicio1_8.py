# Crie um programa que peça ao usuário para digitar um angulo
# entre 0 e 360 graus. Em seguida, o programa deve calcular e mostrar o seno
# cosseno e tangente desse número.

import math

angulo = int(input("Digite um ângulo: "))

seno = math.sin(math.radians(angulo))
print(f"O seno do ângulo {angulo} graus é: {seno}")

cosseno = math.cos(math.radians(angulo))
print(f"O cosseno do ângulo {angulo} graus é: {cosseno}")

tangente = math.tan(math.radians(angulo))
print(f"Tangente do ângulo {angulo} graus é: {tangente}")