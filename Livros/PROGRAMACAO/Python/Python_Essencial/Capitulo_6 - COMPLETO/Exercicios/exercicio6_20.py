# Faça um programa que leia continuamente o número da camisa(chave) 
# e o nome (valor) de jogadores de futebol e armazenando os dados em um dicionário. 
# O programa deve ler até que o usuário digite -1 no número da camisa. 
# Ao fim o programa deve mostrar os jogadores ordenados pelo número da camisa.

jogadores = {}
while True:
    numero = int(input("Digite o Número do Jogador de Futebol: "))
    
    if numero == -1:
        break

    nome_camisa = input("Digite o Nome do Jogador de Futebol: ")
    
    jogadores[numero] = nome_camisa
    
for numero, nome in sorted(jogadores.items()):
    print(f"Camisa {numero}: {nome}")