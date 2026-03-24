# Verificação do horário de funcionamento

dia_da_semana = input("Digite o dia da semana: ")
hora = int(input("Digite a hora atual: "))

if dia_da_semana == "sabado" or dia_da_semana == "domingo" or hora < 9 or hora >= 17:
    print("Loja fechada")
else:
    print("Loja aberta.")
    
# verificação de feriado
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

if dia == 1 and mes == 1 or dia ==25 and mes == 12:
    print("Hoje é feriado.")
else:
    print("Hoje não é feriado.")