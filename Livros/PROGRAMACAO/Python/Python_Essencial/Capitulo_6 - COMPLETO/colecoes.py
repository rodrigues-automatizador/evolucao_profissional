# Exemplo 1
# List comprehension

numeros = [1, 2, 3, 4, 5]

lst_quadrados = [ x ** 2 for x in numeros if x % 2 == 0 ]

dcn_quadrados = { x:x ** 2 for x in numeros if x % 2 == 0 }

cnj_quadrados = { x ** 2 for x in numeros if x % 2 == 0 }

print(lst_quadrados)

print(dcn_quadrados)

print(cnj_quadrados)


# Exemplo 2
# Dict comprehension

numeros = [1, 2, 3, 4, 5]

quadrados = { x: x ** 2 for x in numeros }
print(quadrados)


# Exemplo 3
# Aplicando map e filter a coleções

numeros = [1,2,3,4,5]
quadrados = map(lambda x: x ** 2, numeros)

pares = filter(lambda x: x % 2 == 0, numeros)

print(list(quadrados))

print(list(pares))