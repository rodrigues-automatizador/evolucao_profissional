# Crie um programa que peça ao usuário para inserir um número
# e calcular o fatorial desse número
import math

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = math.factorial(numero)

print(f"O fatorial do {numero} é: {fatorial}")