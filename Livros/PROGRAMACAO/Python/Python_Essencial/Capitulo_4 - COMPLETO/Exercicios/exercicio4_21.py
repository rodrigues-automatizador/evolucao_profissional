# Faça um programa que formate a hora atual 
# no formato de 12 horas incluindo AM/PM

import datetime

data = datetime.datetime.now()

data_formatada = data.strftime("%I:%M %p")

print(data_formatada)