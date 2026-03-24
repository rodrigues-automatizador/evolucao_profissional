# Faça um programa que peça ao usuário para digitar uma lista de nomes e que, 
# em seguida, use mapeamento map para retornar uma nova lista com os nomes em caixa alta.

nomes = input("Digite uma lista de nomes separados por espaço: ").split()

nova_lista_caixa_alta = [list(map(lambda nome: nome.upper(), nomes))]

print(nova_lista_caixa_alta)