# Faça um programa que crie um dicionário com nomes e notas de alunos, 
# ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. 
# Em seguida, use dict compreehension para criar um dicionário
# com os alunos com nota igual ou superior a 7.


dict_aluno = {"Pedro": 6,
              "Maria": 9,
              "João": 8,
              "Ana": 7}

aprovados = {nome: nota for nome, nota in dict_aluno.items() if nota >= 8}

print(aprovados)
