# Crie um programa que peça ao usuário para digitar uma frase
# em seguida, use expressão regular para extrair todos os artigos da frase.
# Ao fim, o programa deve mostrar a frase sem os artigos

frase = input("Digite uma frase: ")
frase = frase.split()

i = 0
while i < len(frase):
    if len(frase[i]) == 1:
        frase.pop(i)
    i += 1

texto = ' '.join(frase)
print(texto)