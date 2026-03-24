# Crie um programa que peça ao usuário para digitar um número inteiro.
# Em seguida, o programa deve calcular e mostrar o valor dos números inteiros
# anterior e posterior a esse número.

valor = int(input("Digite um número: "))

print(f"O valor anterior é: {valor - 1}")
print(f"O valor posterior é: {valor + 1}")