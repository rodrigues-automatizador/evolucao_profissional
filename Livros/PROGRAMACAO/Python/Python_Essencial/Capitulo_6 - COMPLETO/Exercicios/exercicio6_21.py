# Escreva um programa em Python que cria uma lista de strings com 5 nomes de frutas. 
# Use a função random.choice oara escolher uma fruta aleatória da lista e imprimir na tela. 
# Teste seu programa várias vezes para verificar a aleatoriedade da escolha
import random


frutas = ['Maçã', 'Banana', 'Goiaba', 'Pera', 'Melancia']

fruta_aleatoria = random.choice(frutas)
print(fruta_aleatoria)