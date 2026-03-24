# Faça um programa que declare uma lista de 10 números inteiros e inverta a ordem dos elementos 
# de índices pares. Ao fim mostre a lista resultante.

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_indice_pares = [numeros[i] for i in range(0, len(numeros), 2)]
numeros_indice_pares.reverse()

for i in range(0, len(numeros), 2):
    numeros[i] = numeros_indice_pares.pop(0)
    
print(numeros)