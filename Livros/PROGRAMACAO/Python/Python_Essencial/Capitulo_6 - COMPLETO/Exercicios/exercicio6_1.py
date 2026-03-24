# Faça um programa que use uma list compehension para criar uma lista 
# com as raízes quadradas dos números pares de 0 a 20.

import math

raizes = [math.sqrt(x) for x in range(21) if x % 2 == 0]

print(raizes)