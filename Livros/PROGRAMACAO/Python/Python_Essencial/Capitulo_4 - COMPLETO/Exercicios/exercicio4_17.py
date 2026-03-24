# Faça um programa que crie um objeto 
# date que represente a data atual
import datetime

data = datetime.datetime.now()

data_formatada = data.strftime("%d/%m/%Y")
print(f"A data de hoje é: {data_formatada}")
