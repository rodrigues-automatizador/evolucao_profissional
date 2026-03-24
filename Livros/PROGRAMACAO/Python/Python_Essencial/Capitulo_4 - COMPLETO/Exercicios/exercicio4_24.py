# Faça um programa que crie dois objetos datetime, 
# Um representando as 08:00h da manhã e 
# outro representando as 3:00h da tarde do mesmo dia. 
# Calcule a diferença entre esses dois horarios

import datetime

primeiro_horario = datetime.datetime.strptime("08:00", "%H:%M")
segundo_horario = datetime.datetime.strptime("15:00", "%H:%M")

diferenca_horas = segundo_horario - primeiro_horario

print(f"A diferença entre as horas são: {diferenca_horas.seconds / 3600}")