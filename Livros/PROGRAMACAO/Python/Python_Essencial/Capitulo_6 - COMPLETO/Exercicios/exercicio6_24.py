# Desenvolva um jogo de pedra, papel e tesoura. Crie uma lista com as opções mencionadas 
# anteriormente. Utilize a função random.choice para que o computador escolha aleatoriamente 
# entre as opções. O usuário deve inserir a sua escolha e, em seguida,  o programa deve 
# comparar a escolha do usuário com a do computador para determinar o vencedor de acordo 
# com as regras do jogo

import random

lista_janken = ['PEDRA', 'PAPEL', 'TESOURA']

opcao_usuario = input("Digite a opção do jogo JANKEN: ")
opcao_usuario = opcao_usuario.upper()
opcao_computador = random.choice(lista_janken)

if opcao_computador == opcao_usuario:
    print("Empate! Jogue mais uma vez!")
    
elif (
    opcao_computador == "PEDRA" and opcao_usuario == "TESOURA" 
    or opcao_computador == "TESOURA" and opcao_usuario == "PAPEL" 
    or opcao_computador == "PAPEL" and opcao_usuario == "PEDRA"
    ):
    print(f"Você perdeu! Computador: {opcao_computador} vs Usuário {opcao_usuario}" )

else:
    print(f"Você ganhou! Usuário: {opcao_usuario} vs Computador: {opcao_computador}") 