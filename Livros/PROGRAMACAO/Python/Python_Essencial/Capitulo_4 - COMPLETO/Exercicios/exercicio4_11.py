# Crie um programa que peça ao usuário para digitar uma frase
# em seguida fatie a frase em substrings de 6 caracteres e mostre-as uma por linha

frase = input("Digite uma frase: ")

for i in range(0, len(frase), 6):
    print(frase[i:i + 6])