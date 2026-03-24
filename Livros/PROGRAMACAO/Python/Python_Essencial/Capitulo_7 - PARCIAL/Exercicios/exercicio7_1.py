# Crie um programa que solicite ao usuário um nome de arquivo 
# e exiba seu conteúdo na tela.

nome_arquivo = input("Digite o nome do arquivo: ")
path = 'Capitulo_7 - PARCIAL\\Exercicios\\'

with open(path + nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        print(linha)