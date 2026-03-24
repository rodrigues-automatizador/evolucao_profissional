# Faça um programa que declare duas listas de mesmo tamanho, 
# uma com 3 nomes dos alunos e outra com 3 notas. Em seguida, 
# usando a função zip e list compreehension retorne uma lista com 
# as tuplas (nome, nota) em ordem decrescente

nomes = ["Eder", "Tania", "Theo"]
notas = [8, 6, 10]

notas_decrescentes = sorted([(nome, nota) for nome, nota in zip(nomes, notas)], key=lambda x: x[1], reverse=True)

print(notas_decrescentes)