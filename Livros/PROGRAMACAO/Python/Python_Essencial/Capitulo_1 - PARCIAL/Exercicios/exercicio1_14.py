# Crie um programa que peça ao usuário para digitar
# o nome, preço de custo, o preço de venda e a quantidade de estoque de determinado produto
# Em seguida, o programa deve calcular e mostrar o lucro que esse produto
# pode gerar se todo o estoque for vendido

nome_produto = input("Digite o nome do produto: ")
valor_custo = float(input("Digite o preço de custo do produto: "))
valor_venda = float(input("Digite o valor de venda do produto: "))
quantidade_estoque = int(input("Digite a quantidade de estoque do produto: "))

produto = {"nome": nome_produto,
           "custo": valor_custo,
           "revenda": valor_venda,
           "estoque":quantidade_estoque}

calculo_revenda = (produto["revenda"]) - (produto["custo"])
lucro = produto["estoque"] * calculo_revenda

print(f"O produto {produto["nome"]} tem a estimativa de lucro de: {lucro}")
