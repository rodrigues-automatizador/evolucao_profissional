# Faça um programa que crie um objeto datetime representando o instante atual. 
# Em seguida, formate esse instante para exibir o número da semana do ano

import datetime

instante_atual = datetime.datetime.now()

# Utiliza o método wday para apresentar a semana do ano na variavel
resultado = instante_atual.timetuple().tm_wday
print(resultado)