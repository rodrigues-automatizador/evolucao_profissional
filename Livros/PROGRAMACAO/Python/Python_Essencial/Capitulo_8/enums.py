from enum import Enum

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2
    AZUL = 3
    
# Acessando e utilizando um membro Enum

cor_favorita = Cor.AZUL

print(cor_favorita)

print(cor_favorita.name)

print(cor_favorita.value)