

nomes_notas = {"Pedro": 6.5,
               "Maria": 8.7,
               "João":8.3,
               "Ana":7.2}

notas_rredondadas = {nome: round(nota) for nome, nota in nomes_notas.items()}

print(notas_rredondadas)