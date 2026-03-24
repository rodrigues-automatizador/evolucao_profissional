# Crie um programa que encontre e mostre o segundo maior
# e o segundo menor números de uma lista de 10 números

numeros = []
for _ in range(1, 11):
    valor = int(input("Digite 10 números: "))
    numeros.append(valor)

lista_ordenada = sorted(numeros)
segundo_maior = lista_ordenada[-2]
segundo_menor = lista_ordenada[1]

print(lista_ordenada)
print(f"O segundo menor número é: {segundo_menor}")
print(f"O segundo maior número é: {segundo_maior}")