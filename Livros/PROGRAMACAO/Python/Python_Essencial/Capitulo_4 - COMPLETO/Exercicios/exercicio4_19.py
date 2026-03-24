# Faça um programa que crie um objeto datetime representando 
# dia 15 de janeiro de 2022 as 12:00
# Versão 1

import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
 
agora = datetime.datetime.now()
 
ano = agora.strftime("%Y") 
mes = agora.strftime("%B")
dia = agora.strftime("%d")
hora = agora.strftime("%H:%M")
 
print(f"Dia {dia} de {mes} de {ano} às {hora}")