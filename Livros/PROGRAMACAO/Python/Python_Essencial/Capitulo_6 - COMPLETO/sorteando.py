import random

# Exemplo 1
# Sorteando itens de uma lista

lista = [1,2,3,4,5]

elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)


# Exemplo 2
# Sorteando caracteres de um texto.

string = "Olá, mundo!"

caractere_aleatorio = random.choice(string)

print(caractere_aleatorio)


# Exemplo 3
# Sorteando itens de uma tupla

tupla = ("maçã", "banana", "cereja")
item_aleatorio = random.choice(tupla)

print(item_aleatorio)


# Exemplo 4
# Sorteando chaves de um dicionário

dicionario = {"nome":"João",
              "idade":25,
              "cidade":"São Paulo"}

chaves = list(dicionario.keys())
chave_aleatoria = random.choice(chaves)

print(chave_aleatoria)


# Exemplo 3
# Lista gerada a partir de instruções yield

def lista_gerada():
    yield 1
    yield 2
    yield 3
    
lg = lista_gerada()

print(next(lg))

print(next(lg))

print(next(lg))


# Exemplo 4
# Generator sequencia de fibonacci

def fibonacci():
    a, b = 0, 1
    
    while True:
        yield a 
        a, b = b, a + b
        
f = fibonacci()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))