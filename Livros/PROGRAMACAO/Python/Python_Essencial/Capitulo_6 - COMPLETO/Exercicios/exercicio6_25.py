# Desenvolva um programa que simule um sorteio de nomes para um amigo secreto. 
# Cada pessoa só pode tirar outra pessoa uma vez e uma pessoa não pode tirar a si mesma. 
# O programa deve continuar sorteando até que todas as pessoas tenham tirado um amigo secreto. 
# Utilize a função random.choice para realizar o sorteio. As pessoas participantes são: 
# Alice, "Bruno", "Carlos", "Daniela", "Fabiana", "Gustavo", "Helena", "Juliana". Ao final, 
# o programa deve exibir quem tirou quem no amigo secreto.

import random

participantes = ["Alice", "Bruno", "Carlos", "Daniela", "Fabiana", "Gustavo", "Helena", "Juliana"]
amigo_secreto = {}

for p in participantes:
    possiveis = list(set(participantes) - set([p]) - set(amigo_secreto.values()))
    amigo_secreto[p] = random.choice(possiveis)
    
for p, a in amigo_secreto.items():
    print(f"{p} tirou {a}")