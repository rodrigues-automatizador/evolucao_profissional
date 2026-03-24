# Crie um programa que peça ao usuário para digitar
# 3 números e imprima a soma do dobro de cada um deles.

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

resultado = ((valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3))
print(f"O dobro da soma de todos os valores é: {resultado}")