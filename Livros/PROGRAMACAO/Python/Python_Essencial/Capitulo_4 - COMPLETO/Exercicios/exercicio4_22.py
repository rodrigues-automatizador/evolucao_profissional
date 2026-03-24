# Crie um programa que formate o instante atual para mostrá-las 
# no formato "terça-feira, 13 de junho de 2023, 19:22"

import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

data = datetime.datetime.now()

hora = data.strftime("%H:%M")
dia = data.strftime("%d")
dia_semana = data.strftime("%A")
mes = data.strftime("%B")
ano = data.strftime("%Y")

print(f"{dia_semana}, {dia} de {mes} de {ano}, {hora}.")