# Crie um programa que some e mostre todos os numeros pares de 1 a 100

soma = 0
for numero in range(0, 101):
    if numero % 2 == 0:
        soma += numero
        print(soma)