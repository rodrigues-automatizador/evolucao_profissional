# Exemplo 1

try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
    
except FileNotFoundError as erro:
    raise ValueError("Erro ao ler arquivo") from erro

# Exemplo 2
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
    
except ValueError as erro2:
    print("Erro: " + str(erro2))
    if erro2.__cause__:
        print("Causa do erro: " + str(erro2.__cause__))