# Crie um programa que peça ao usuário para digitar 5 números inteiros.
# O programa deve exibir uma mensagem informando se todos os números são pares
# ou se há pelo menos um número ímpar

contador = 0

for _ in range(0, 5):
    numero = int(input("Digite um número: "))
        
    if numero % 2 != 0:
        contador += 1
        
if contador == 0:
    print("Todos os números são pares!")
else:
    print(f"Existem {contador} números ímpares!")