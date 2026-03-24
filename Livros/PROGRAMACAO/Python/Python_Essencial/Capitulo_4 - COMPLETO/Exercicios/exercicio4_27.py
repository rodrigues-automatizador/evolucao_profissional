# Faça um programa que crie um objeto datetime representando um instante específico. 
# Em seguida, adicione 2 dias e 5 horas a esse mesmo instante utilizando timedelta

import datetime

data = datetime.datetime.now()

data_atualizada = datetime.timedelta(days=2)
resultado = data + data_atualizada

hora_atualizada = datetime.timedelta(hours=5)
resultado = resultado + hora_atualizada

resultado = resultado.strftime("%d/%m/%Y %H:%M:%S")

print(resultado)