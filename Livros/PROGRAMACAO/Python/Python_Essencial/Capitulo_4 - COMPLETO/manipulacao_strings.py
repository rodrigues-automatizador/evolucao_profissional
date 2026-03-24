import re

# Exemplo 1

texto = "Python é uma linguagem de programação popular. Python é fácil de aprender e usar"

novo_texto = texto.replace("Python", "Java")
print(novo_texto)

# Exemplo 2

texto = "Este é Um TexTo com leTrAs MaIúsCulas e miNúsCulAs."

# Letras minúsculas
texto_min = texto.lower()

# Letras maiúsculas
texto_mai = texto.upper()

# imprime texto minúsculo
print(texto_min)

# imprime texto maiúsculo
print(texto_mai)


# Exemplo 3
# Extração de strings

texto = "Este é um exemplo de texto."

palavras = texto.split()

print(palavras)

# Exemplo 4
# Utilizando o método slice

texto = "Este é um exemplo de texto."
parte = texto[slice(5, 18)]

print(parte)

# Exemplo 5
# Verificação de strings

texto = "Este é um exemplo de texto."

if texto.startswith("Este"):
    print("A string começa com 'Este'.")
else:
    print("A string não começa com 'Este'.")
    
if texto.endswith("texto."):
    print("A string termina com 'texto.'")
else:
    print("A string não termina com 'texto.'")
    
    
# Exemplo 6
# remoção de espaços em branco

texto = "             Este é um exemplo de texto."
texto_sem_espaco = texto.strip()

print(texto_sem_espaco)


# Exemplo 7
# Localização de strings

texto = "Este é um exemplo de texto."
posicao = texto.find("exemplo")
print(posicao)

# Exemplo 8
# Contagem de ocorrências de uma substring.

texto = "Este é um exemplo de texto. Este texto é sobre Python"

num_ocorrencias = texto.count("Este")
print(num_ocorrencias)


# Exemplo 9
# Quantidade de caracteres em uma string

texto = "Texto qualquer."
qtde_caracteres = len(texto)
print(qtde_caracteres)


# Exemplo 10
# Expressões regulares - Substituição.

texto = "Python 3 é incrível!"
novo_texto = re.sub(r"\d", "4", texto)

print(novo_texto)


# Exemplo 11
# Expressões regulares - busca.
texto = "Aprender Python é divertido."
busca = re.search("Python", texto)

if busca:
    print("Padrão encontrado!")
    
else:
    print("Padrão não encontrado.")
    

# Exemplo 12
# Verifica se o início de uma string corresponde a um padrão.
 
texto = "Python é poderoso."

if re.match("Python", texto):
    print("Começa com Python.")
    
else:
    print("Não começa com Python.")
    
    
# Exemplo 13
# Método full match

texto = "Python"

if re.match("Python", texto):
    print("A string é exatamente 'Python'")
else:
    print("A string é diferente de 'Python'")
    

# Exemplo 14
# Utilizando o método findall
texto = "Python 3, Python 2, Python 1"

versoes = re.findall(r"Python \d", texto)

print(versoes)