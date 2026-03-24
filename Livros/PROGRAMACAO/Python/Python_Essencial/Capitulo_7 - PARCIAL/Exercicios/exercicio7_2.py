# Crie um programa que leia um arquivo texto, 
# e exiba quantas linhas ele possui.

path = 'Capitulo_7 - PARCIAL\\Exercicios\\'

with open(path + 'meu-arquivo2.txt','r') as arquivo:
    for linhas in arquivo:
        print(linhas)