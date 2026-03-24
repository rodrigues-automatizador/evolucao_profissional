# Faça um programa que declare uma lista de 10 números inteiros e um número de 
# referencia pertencente a lista. Ao fim, retorne uma nova lista contendo os itens da 
# lista original que tenham valor superior ao número de referencia.

lista_original = [1,2,3,4,5,6,7,8,9,10]

numero_referencia = 8
nova_lista = [numero for numero in lista_original if numero > numero_referencia] 

print(nova_lista)