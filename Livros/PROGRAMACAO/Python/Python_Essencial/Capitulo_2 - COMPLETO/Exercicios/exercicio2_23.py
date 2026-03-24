# Desenvolva um tradutor de emoções que peça ao usuário para inserir uma emoção
# (feliz, triste, nervoso etc.) 

emocao = input("Digite o seu sentimento: ")
emocao = emocao.upper()

match emocao:
    case "FELIZ":
        print(":)")
        
    case "TRISTE":
        print(":()")
        
    case "ANIMADO":
        print(";)")
        
    case _:
        print("Poker face!")