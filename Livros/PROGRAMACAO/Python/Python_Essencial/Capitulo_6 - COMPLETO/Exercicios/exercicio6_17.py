# Faça um programa que declare uma lista com ao menos 10 números inteiros, 
# com pelo menos 3 deles repetidos. Em seguida, converta essa lista para um conjunto, 
# visando eliminar os itens repetidos, converta de volta para uma lista, 
# e mostre o resultado na tela

lista_numeros = [10,5,6,6,3,7,5,3,4,8]

conjunto = set(lista_numeros)
lista = list(conjunto)
print(lista)
