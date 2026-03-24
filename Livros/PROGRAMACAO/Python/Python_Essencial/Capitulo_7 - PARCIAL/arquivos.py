# Exemplo 1
# Criando arquivo txt

arquivo = open("meu-arquivo.txt", "w")
arquivo.write("Este é o conteúdo do meu arquivo")
arquivo.close()


# Exemplo 2
# Leitura de um arquivo linha por linha

arquivo = open('Capitulo_7 - PARCIAL\\arquivo.txt', 'r')
linha = arquivo.readline()

while linha:
    print(linha)
    linha = arquivo.readline()
    
arquivo.close()

# Exemplo 3
with open('meu-arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)