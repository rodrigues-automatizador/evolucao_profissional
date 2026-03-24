# Faça um programa com duas listas contendo 3 valores cada, um com chaves (string) 
# e outra com os valores (int), e retorne um dicionário criado a partir dessas duas listas

chaves = ["chave1", "chave2", "chave3"]
valores = [1, 2, 3]

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}

print(dicionario)