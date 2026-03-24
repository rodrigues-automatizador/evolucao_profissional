# Faça um programa que use list compreehnsion para criar uma lista 
# com os números divisíveis por 3 ou 5 de 0 a 30

lista_numeros = [x for x in range(31) if x % 3 == 0 or x % 5 == 0]

print(lista_numeros)