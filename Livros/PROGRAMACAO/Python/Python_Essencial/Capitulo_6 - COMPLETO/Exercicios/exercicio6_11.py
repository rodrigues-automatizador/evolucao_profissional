# Faça um programa que peça ao usuário para digitar uma lista de números e que, 
# em seguida, use filtragem para retornar uma nova lista com os números pares.

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split(",")))

lista_par = list(filter(lambda x: x % 2 == 0, numeros))

print(lista_par)