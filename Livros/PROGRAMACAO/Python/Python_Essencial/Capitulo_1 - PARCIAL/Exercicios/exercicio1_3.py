# Crie um programa que peça ao usuário para digitar
# 3 números, armazenando-os em variáveis distintas.
# Em seguida imprima a média aritmética dos 3 números.

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

resultado = ((valor1 + valor2 + valor3) / 3)
print(f"A média dos valores inseridos é: {resultado}")