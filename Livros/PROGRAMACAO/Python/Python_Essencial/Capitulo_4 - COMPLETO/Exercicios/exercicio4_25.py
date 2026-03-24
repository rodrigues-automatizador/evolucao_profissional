# Faça um programa que adicione 30 dias 
# à data atual utilizando timedelta

import datetime

data_atual = datetime.datetime.now()
dias_acrescentados = datetime.timedelta(days=30)

data_atualizada = data_atual + dias_acrescentados

print(f"A data foi atualizada para: {data_atualizada}")
