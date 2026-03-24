# tupla_vazia
tupla_vazia = ()
print(tupla_vazia)

# tupla com elementos
tupla = 1,2,3,4
print(tupla)

# tupla com elementos demilimitada por parenteses
tupla = (1,2,3,4)
print(tupla)

# acessando elementos em uma tupla
tupla = (1,2,3,4)
print(tupla[0])

print(tupla[-1])

# tupla com elementos de diferentes tipos
tupla = (1,2, "três", 4.0)
print(tupla)

# fatiamento de tuplas
tupla = (1,2,3,4,5)
print(tupla[1:3])

print(tupla[:-2])

# desempacotamento de tuplas
tupla = (1,2,3)
a, b, c = tupla
print(a)
print(b)
print(c)

# concatenação de tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

# funções nativas
tupla = (1,2,3,4,5)
print(len(tupla))

print(min(tupla))

print(max(tupla))

print(sum(tupla))