# Crie um programa que solicite ao usuário digitar uma descrição do clima
# (ensolarado, chuvoso, nublado etc...) e utilize a estrutura match case
# para imprimir uma sugestão de roupa

clima = input("Digite o tempo (Clima): ")

clima = clima.upper()

match clima:
    case "ENSOLARADO":
        print("Utilize bermuda e óculos de sol!")
        
    case "CHUVOSO":
        print("Levar guarda chuvas e capa!")
        
    case "NUBLADO":
        print("Levar uma blusa de frio!")
        
    case _:
        print("Utilize roupa padrão ou fique em casa!")