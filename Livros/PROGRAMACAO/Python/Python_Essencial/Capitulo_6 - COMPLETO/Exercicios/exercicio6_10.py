# Faça um programa que peça ao usuário para digitar uma lista de palavras e que, 
# em seguida, use mapeamento (map()) para retornar uma nova lista 
# com os comprimentos de cada palavra

palavras = input("Digite uma lista de palavras separadas por espaço: ")
palavras = palavras.split()

tamanho_palavras = [list(map(len, palavras))]

print(tamanho_palavras)