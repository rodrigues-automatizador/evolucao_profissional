# Crie um programa que peça ao usuário para digitar uma frase com 5 palavras.
# Caso a frase digitada tenha uma quantidade diferente de palavras,
# o usuário deve digitar novamente. Ao fim, mostre uma palavra por linha.

while True:
    frase = input("Digite uma frase: ")
    frase = frase.split()
    
    if len(frase) < 5:
        print("Você deve digitar no mínimo 5 palavras!")
        
    else:
        # Condição para encerrar o loop
        break

for palavras in frase:
    print(palavras)