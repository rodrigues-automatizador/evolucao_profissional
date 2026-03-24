# Crie um programa que calcule e mostre o fatorial
# de um número digitado pelo usuário.
import math

numero = int(input("Digite um número para descobrir o fatorial: "))

fatorial = math.factorial(numero)

print(f"O fatorial de {numero} é: {fatorial}")