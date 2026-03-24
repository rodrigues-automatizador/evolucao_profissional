# Faça um programa que crie dois objetos datetime, um que represente o 
# dia 1 de janeiro de 2022 e o outro representando o dia 1 de fevereiro de 2022. 
# Calcule e mostre a diferença entre essas duas datas em dias

import datetime

primeira_data = datetime.date(2022, 1, 1)
segunda_data = datetime.date(2022, 1, 2)

diferenca = segunda_data - primeira_data

print(f"A diferença de dias são: {diferenca.days}")