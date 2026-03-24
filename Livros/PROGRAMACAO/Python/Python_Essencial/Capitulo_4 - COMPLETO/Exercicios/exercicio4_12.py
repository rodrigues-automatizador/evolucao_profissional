# Crie um programa que peça ao usuário para digitar uma frase e que,
# em seguida, verifique quantas palavras terminam com a letra "o"
# e quantas terminam com a letra "a".

frase = input("Digite uma frase: ")
frase = frase.split()

i = 0
letra_a = 0
letra_o = 0

while i < len(frase):
    if frase[i].endswith("a") == True:
        letra_a += 1

    if frase[i].endswith("o") == True:
        letra_o += 1
        
    i += 1

print(f"A quantidade de palavras que terminam com a letra A é: {letra_a}")
print(f"A quantidade de palavras que terminam com a letra O é: {letra_o}")