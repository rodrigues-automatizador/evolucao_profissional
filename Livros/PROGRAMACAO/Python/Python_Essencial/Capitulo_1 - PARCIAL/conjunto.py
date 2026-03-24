# criação direta de um conjunto
conjunto = {1,2,3,4}

print(conjunto)

# criação de um conjunto a partir de uma lista usando a função set
conjunto = set([1,2,3,4])
print(conjunto)

conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}

# uniao
print(conjunto1 | conjunto2)

# interseção
print(conjunto1 & conjunto2)

# diferença
print(conjunto1 - conjunto2)