# Neste exercicio você vai criar um jogo de perguntas e respostas. 
# As perguntas e suas respectivas respostas devem ser armazenadas em um dicionário, 
# onde as chaves são as perguntas e os valores são as respostas. Escreva um programa 
# que escolhe uma pergunta aleatória e a imprime na tela. O usuário deve então tentar
# responder à pergunta, e o programa deve informar se a resposta está correta ou não.

import random
perguntas_respostas = {"Qual a capital do Brasil?":"Brasilia", 
                       "Qual é a moeda do Japão?":"Iene",
                       "Qual é o maior planeta do sistema solar?":"Jupiter"}

pergunta = random.choice(list(perguntas_respostas.keys()))

print(pergunta)
resposta = input("Digite a sua resposta: ")

if resposta.lower() == perguntas_respostas[pergunta].lower():
    print("Resposta correta")
else:
    print(f"Resposta incorreta. A resposta correta é: {perguntas_respostas[pergunta]}")