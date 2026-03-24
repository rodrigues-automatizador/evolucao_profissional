# Crie um programa que gere um número aleatorio entre 1 e 10
# e peça ao usuário para tentar adivinhar o número.
# Em caso de erro, o programa deve informar se o número digitado pelo usuário
# é maior ou menor do que o número gerado

import random

numero = int(input("Tente adivinha, escolha um número de 1 a 10: "))

numero_sorteado = random.randint(1, 10)

if numero == numero_sorteado:
    print("Parabéns você acertou!")
    
elif numero != numero_sorteado:
    if numero > numero_sorteado:
        print("Você errou! Número sorteado é menor!")
    else:
        print("Você errou! Número sorteado é maior!")
        
    print(numero_sorteado)
    
else:
    print("Número inválido!")