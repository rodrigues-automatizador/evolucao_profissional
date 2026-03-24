# Autenticação de usuário
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "123":
    print("Você tem permissão de acesso.")
else:
    print("Você não tem permissão de acesso.")
    
# Verificação de horario de trabalho
hora = int(input("Digite a hora atual: "))
dia = input("Digite o dia da semana: ")

if hora >= 9 and hora <=18 and dia != "sabado" and dia != "domingo":
    print("Você está no horario de trabalho.")
else:
    print("Você não está no horário de trabalho.")