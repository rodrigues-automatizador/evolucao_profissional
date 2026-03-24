# Crie um generator que simule um fluxo de dados capturados de um sensor. 
# O sensor gera uma leitura (um número aleatório entre 0 e 100) a cada iteração. 
# Use o generator para imitar a leitura do sensor 10 vezes.

import random

def leitura_sensor():
    while True:
        yield random.randint(0, 100)
        
generator = leitura_sensor()

for i in range(10):
    print(next(generator))