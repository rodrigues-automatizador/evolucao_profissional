# Escreva um programa que peça ao usuário para inserir uma faixa etária,
# em seguida, utilize a estrutura match case para sugerir um filme adequado para a idade
# Você pode categorizar as faixas etárias e sugerir diferentes tipos de filmes.

faixa_etaria = input("Digite sua faixa etária: ")
faixa_etaria = faixa_etaria.upper()

match faixa_etaria:
    case "IDOSO":
        print("Assistir Chacrinha ou Mazaroppi!")
        
    case "INFANTIL":
        print("Assistir Bom dia & CIA!")
        
    case "ADOLESCENTE":
        print("Assista animes!")
        
    case "ADULTO":
        print("Assista filmes categoria Drama, Suspense e Terror!")
        
    case _:
        print("Assista Chaves!")
        

