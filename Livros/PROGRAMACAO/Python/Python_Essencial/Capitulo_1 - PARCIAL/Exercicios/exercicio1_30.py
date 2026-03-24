# Crie um programa que tenha 2 conjuntos de 5 números quaisquer e combine-os
# usando as operações de união, interseção e diferença,
# apresentando os resultados de cada operação

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,2,13,14,15}

print("União de conjuntos: ", conjunto1 | conjunto2)
print("Interseção de conjuntos: ", conjunto1 & conjunto2)
print("Diferença de conjuntos: ", conjunto1 - conjunto2)