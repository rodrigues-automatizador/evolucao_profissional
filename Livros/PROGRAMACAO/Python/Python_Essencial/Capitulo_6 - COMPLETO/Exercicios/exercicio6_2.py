# Faça um programa que use list compreehension para criar uma lista com as palavras 
# que contém a letra "a" em uma frase digitada pelo usuário, substituindo a letra por "o"

frase = input("Digite uma frase: ")

lista_palavras_modificadas = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]

print(lista_palavras_modificadas)