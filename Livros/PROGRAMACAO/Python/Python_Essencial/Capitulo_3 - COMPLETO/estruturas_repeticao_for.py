# Exemplo 1
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# Exemplo 2    
numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero

print("A soma dos números é", soma)

# Exemplo 3
nome = "João"
for letra in nome:
    print(letra)
    
# Exemplo 4
numero = 5
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
    
print("O fatorial de", numero, "é", fatorial)

cores = ['vermelho','verde','azul']

# Iterando sobre a lista com índices
for indice, cor in enumerate(cores):
    print(f"Índice {indice}: {cor}")
    
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)