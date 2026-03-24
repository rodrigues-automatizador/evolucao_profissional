# Crie um programa que calcule e mostre a tabuada de um número

tabuada = int(input("Digite a número para calcular a tabuada: "))

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")