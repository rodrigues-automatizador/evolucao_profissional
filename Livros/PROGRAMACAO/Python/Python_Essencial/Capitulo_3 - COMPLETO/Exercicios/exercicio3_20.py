# Crie um programa que calcule e mostre o fatorial de todos os números
# de 1 a n, onde n é digitado pelo usuário
import math

fatorial = int(input("Digite quantos números fatoriais quer calcular: "))

numero = 1
while numero <= fatorial:
    resultado = math.factorial(numero)
    
    print(f"O fatorial de {numero} é: {resultado}")
    numero += 1