# Você é um sommelier em um restaurante de alto padrão e tem uma lista longa de vinhos, 
# cada um com um preço diferente. O seu gerente lhe deu uma tarefa: Encontrar os vinhos mais caros da 
# lista para uma degustação especial. Para isso, você vai precisar de uima função que possa filtrar 
# os vinhos por preço. Como a lista de vinhos está sempre mudando, essa função precisa ser flexível 
# e fácil de alterar. Escreva um programa que crie uma lista de vinhos onde cada vinho é representado 
# por um dicionário com o nome e o preço do vinho. Em seguida, use uma função lambda para criar uma nova 
# lista contendo apenas os vinhos que custam mais de 50 reais. Imprima esta nova lista de vinhos caros.

vinhos = [{"nome":"Vinho A","preco": 45,
           "nome":"Vinho B","preco": 80,
           "nome":"Vinho C","preco": 30,
           "nome":"Vinho D","preco": 60,
           "nome":"Vinho E","preco": 120}]

vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))

print(vinhos_caros)