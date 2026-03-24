# Crie um programa que mostre a data atual 
# no formato "DD-MM-AAAA"

import datetime

data = datetime.datetime.now()
print(data.strftime("%d-%m-%Y"))