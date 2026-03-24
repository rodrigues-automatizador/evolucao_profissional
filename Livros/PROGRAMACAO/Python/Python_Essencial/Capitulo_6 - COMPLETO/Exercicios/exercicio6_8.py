# Faça um programa que peça ao usuário para digitar uma lista de números 
# e que use o mapeamento map() para retornar uma nova lista com os quadrados de cada número

lista_numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

numeros_quadrados = list(map(lambda n: n ** 2, lista_numeros))

print(numeros_quadrados)