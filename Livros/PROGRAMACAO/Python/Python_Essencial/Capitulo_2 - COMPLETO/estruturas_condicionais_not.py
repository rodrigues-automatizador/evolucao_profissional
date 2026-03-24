# Verificação de maioridade
idade = int(input("Digite sua idade: "))

if not idade >= 18:
    print("Você não tem mais de 18 anos.")
else:
    print("Você tem mais de 18 anos.")
    
    
# Verificação de horário de trabalho
hora = int(input("Digite a hora atual: "))

if not (hora >= 9 and hora <=18):
    print("Você não está no horário de trabalho.")
    
else:
    print("Você está no horário de trabalho.")