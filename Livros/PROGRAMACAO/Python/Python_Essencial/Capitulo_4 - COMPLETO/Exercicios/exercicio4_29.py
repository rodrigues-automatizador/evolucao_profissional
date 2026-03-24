# Faça um programa que crie um objeto datetime que represente o instante atual. 
# Em seguida, formate esse instante para exibiro número do dia do ano entre 1 e 365.

import datetime

instante_atual = datetime.datetime.now()

# Utiliza o método yday para apresentar o dia do ano na variavel
resultado = instante_atual.timetuple().tm_yday
print(resultado)