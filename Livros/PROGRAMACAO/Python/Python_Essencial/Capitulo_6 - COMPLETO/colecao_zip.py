# Exemplo 1
# Utilizando função zip

nomes = ["João", "José", "Maria", "Pedro"]
idades = [25, 30, 20] 

pessoas = zip(nomes, idades)

for nome, idade in pessoas:
    print(f"{nome} tem {idade} anos.")
    

# Exemplo 2
# Operações do tipo Conjuntos

numeros1 = [1,2,3,4,5]
numeros2 = [3,4,5,6,7]

conjunto1 = set(numeros1)
conjunto2 = set(numeros2)

uniao = conjunto1.union(conjunto2)
intersessao = conjunto1.intersection(conjunto2)
diferenca = conjunto1.difference(conjunto2)

print(uniao)
print(diferenca)
print(intersessao)


# Exemplo 3
# Acessando um elemento único em uma lista

lista = [1,2,3,4,5]

primeiro_elemento = lista[0]
terceiro_elemento = lista[2]

print(primeiro_elemento)
print(terceiro_elemento)


# Exemplo 4
# Acessando um caractere único em uma string

frase = "Hello, World!"

primeiro_caractere = frase[0]
ultimo_caractere = frase[-1]

print(primeiro_caractere)
print(ultimo_caractere)


# Exemplo 5
# Acessando um intervalo de elementos

lista = [1,2,3,4,5]
primeiro_tres_elementos = lista[0:3]
elementos_do_meio = lista[1:4]

print(primeiro_elemento)
print(elementos_do_meio)


# Exemplo 6
# Acessando um intervalo de caracteres em uma string

frase = "Hello, World!"

primeiros_caracteres = frase[0:5]
caracteres_do_meio = frase[7:12]

print(primeiros_caracteres)
print(caracteres_do_meio)


# Exemplo 7
# Acessando elementos a partir do final da coleção

lista = [1,2,3,4,5]

ultimo_elemento = lista[-1]

penultimo_elemento = lista[-2]

print(ultimo_elemento)

print(penultimo_elemento)


# Exemplo 8
# Acessando caracteres a partir do final de uma string

frase = "Hello, World!"

ultimo_caractere = frase[-1]
penultimo_caractere = frase[-2]

print(ultimo_caractere)
print(penultimo_caractere)


# Exemplo 9
# Acessando intervalos de elementos usando passo

lista = [1,2,3,4,5]

elementos_com_passo = lista[0:5:2]
print(elementos_com_passo)


# Exemplo 10
# Acessando caracteres de uma string com passo

frase = "Hello, World!"

caracteres_com_passo = frase[0:12:2]
print(caracteres_com_passo)


# Exemplo 11
# Acessando elementos de forma invertida.

lista = [1,2,3,4,5]
elementos_reversos = lista[::-1]
print(elementos_reversos)


# Exemplo 12
# Acessando os caracteres de uma string de forma reversa

frase = "Hello, World!"
caracteres_reversos = frase[::-1]

print(caracteres_reversos)