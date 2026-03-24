# Faça um programa que declare duas listas com 5 valores inteiros cada. 
# Usando a função zip e list compreehension retorne uma terceira lista 
# com a média dos elementos do mesmo índice

lista_numero1 = [1,2,3,4,5]
lista_numero2 = [6,7,8,9,10]

media_listas = [(a + b) / 2 for a, b in zip(lista_numero1, lista_numero2)]

print(media_listas)