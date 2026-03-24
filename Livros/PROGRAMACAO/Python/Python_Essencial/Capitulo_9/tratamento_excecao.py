# Exemplo 1

try:
    x = 1 / 0
    
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
    
    
# Exemplo 2
try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
    
    
# Exemplo 3
try: 
    x = int(input("Digite um número inteiro: "))
    resultado = 10 / x
    
except ZeroDivisionError:
    print("Erro: divisão por zero!")
    
except ValueError:
    print("Erro: valor inválido!")
    
    
# Exemplo 4
arquivo = None
try:
    arquivo = open("arquivo.txt","r")
    conteudo = arquivo.read()
    
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
    
finally:
    if arquivo is not None:
        arquivo.close()