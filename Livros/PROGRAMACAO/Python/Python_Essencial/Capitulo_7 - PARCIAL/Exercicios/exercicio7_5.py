# Crie um arquivo vazio qualquer. Agora crie um programa que solicite ao usuário 
# que digite o nome desse arquivo e exclua-o.

import os

nome_arquivo = input("Digite o nome do arquivo: ")
path = 'Capitulo_7 - PARCIAL\\Exercicios\\'

arquivo = open(path + nome_arquivo, 'w')
arquivo.close()

excluir = input("Digite SIM para exluir arquivo: ")

if excluir.upper() == 'SIM':
    os.remove(path + nome_arquivo)

