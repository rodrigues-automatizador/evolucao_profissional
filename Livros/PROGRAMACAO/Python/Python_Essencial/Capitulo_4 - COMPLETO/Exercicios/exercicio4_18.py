# Faça um programa que crie um objeto 
# time que represente a hora atual

import datetime

data = datetime.datetime.now()

hora_atual = data.strftime("%H:%M:%S")
print(f"A hora atual é: {hora_atual}")