# Crie um programa que peça ao usuário para digitar uma palavra.
# O programa deve então indicar se a palavra inserida começa com uma vogal ou uma consoante.

palavra = input("Digite uma palavra: ")

vogal = palavra[:1]
vogal = vogal.upper()

if vogal == "A" or vogal == "E" or vogal == "I" or vogal == "O" or vogal == "U":
    print(f"A primeira letra da palavra digitada é uma vogal {vogal}")
    
else:
    print(f"A primeira letra da palavra digitada é uma consoante {vogal}")