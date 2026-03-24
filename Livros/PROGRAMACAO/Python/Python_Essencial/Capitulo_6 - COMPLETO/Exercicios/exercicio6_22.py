# Considere uma string que contém todas as letras do alfabeto. Escreva um programa em Python 
# que use a função random.choice para escolher continuamente 
# uma letra até que todas as letras do seu nome tenham sido sorteadas. ao fim, 
# mostre a quantidade de sorteios que foram necessários.

import random

letras = 'abcdefghijklmnopqrstuvwxyz'

nome = 'rodrigues'

letras_nome = set(nome)
sorteios = 0

letras_sorteadas = ''

while set(letras_sorteadas) != set(letras_nome):
    letra = random.choice(letras)
    
    if letra in letras_nome and letra not in letras_sorteadas:
        letras_sorteadas += letra
    sorteios += 1
        
print(nome, letras_sorteadas)
print(sorteios)