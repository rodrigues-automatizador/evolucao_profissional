# Crie um programa que peça ao usuário para digitar uma frase, divida-a em palavras,
# remova todos os espaços em branco desnecessários dessas palavras, e componha a frase
# novamente com apenas 1 espaço entre palavras

frase = input("Digite uma frase: ")

frase = frase.split()
resultado = ' '.join(frase)

print(resultado)