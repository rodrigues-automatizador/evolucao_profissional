# Faça um programa que subtraia 2 horas da hora atual utilizando o timedelta

import datetime

hora_atual = datetime.datetime.now()

horas_atualizadas = hora_atual - datetime.timedelta(hours=2)
print(horas_atualizadas)