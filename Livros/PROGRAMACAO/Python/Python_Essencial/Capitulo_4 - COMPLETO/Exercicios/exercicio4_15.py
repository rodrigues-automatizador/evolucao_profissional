# Crie um programa que peça ao usuário para digitar uma frasee que,
# em seguida, mostre quantas vezes cada palavra aparece
# Versão 1
# Crie um programa que peça ao usuário para digitar uma frasee que,
# em seguida, mostre quantas vezes cada palavra aparece

frase_original = input("Digite uma frase: ")

palavras = frase_original.split()
palavras = list(dict.fromkeys(palavras))

i = 0
while i < len(palavras):
    contagem = frase_original.count(palavras[i])
    print(f"A palavra {palavras[i]} aparece: {contagem}")
    i += 1


# Versão 2

frase_original = input("Digite uma frase: ")
frase = frase_original.split()

sem_repeticao = []
for item in frase:
    if item not in sem_repeticao:
        sem_repeticao.append(item)

i = 0
while i < len(sem_repeticao):
    contagem = frase_original.count(sem_repeticao[i])
    print(f"A palavra {sem_repeticao[i]} aparece: {contagem}")
    i += 1