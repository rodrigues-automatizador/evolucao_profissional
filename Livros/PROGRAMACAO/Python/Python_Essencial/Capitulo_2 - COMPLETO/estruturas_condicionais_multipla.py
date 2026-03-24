linguagem = input("Qual é a linguagem que você tem maior domínio? ")

match linguagem:
    
    case "Python":
        print("Muito usada em IoT e Inteligência Artificial.")
        
    case "Javascript":
        print("Muito usada em desenvolvimento WEB.")
        
    case "C#":
        print("Muito usada em aplicações em geral.")
        
    case _:
        print("A linguagem não importa, o que importa é resolver problemas.")