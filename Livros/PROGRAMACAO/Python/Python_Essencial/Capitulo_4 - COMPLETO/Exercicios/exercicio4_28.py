# Faça um programa que crie dois objetos datetime, 
# um representando o instante atual e outro representando um instante no futuro. 
# Verifique se o instante atual é realmente anterior ao instante futuro.

import datetime

instante_atual = datetime.datetime.now()

atualizacao_instante = datetime.timedelta(minutes=30)
instante_futuro = instante_atual + atualizacao_instante

if instante_futuro > instante_atual:
    print("Tempo está no futuro!")
    
else:
    print("Tempo está no passado!")