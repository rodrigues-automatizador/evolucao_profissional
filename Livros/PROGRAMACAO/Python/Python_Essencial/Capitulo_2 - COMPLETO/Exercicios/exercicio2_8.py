# Crie um programa que verifique se um texto digitado pelo usuário corresponde
# a uma data no formato "DD/mm/aaaa", considerando que a data deve ter 10 caracteres,
# "dd" deve variar de 01 a 31, "mm" de 01 a 12 e "aaaa" de 0001 a 9999.

data = input("Digite uma data no formato DD/MM/AAAA: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if dia < 1 or dia > 31:
    print("Dia inválido.")
    
elif mes == 2 and dia >= 30:
    print("Fevereiro tem apenas 29 dias!")

elif mes < 1 or mes > 12:
    print("Mês inválido.")
    
elif ano < 1 or ano > 9999:
    print("Ano inválido.")
    
else:
    print(f"A data informada é: {dia} / {mes} / {ano}")