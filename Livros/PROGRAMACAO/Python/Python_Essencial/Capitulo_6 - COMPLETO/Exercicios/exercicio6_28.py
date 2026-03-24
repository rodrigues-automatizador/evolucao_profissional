# Implemente um generator chamado "pega palavras" que receba um texto e retorne, 
# a cada iteração, uma palavra desse texto (considerando que as palavras são
# separadas por espaço). Teste seu generator com uma frase a sua escolha.

def pega_palavras(texto):
    palavras = texto.split(" ")
    
    for palavra in palavras:
        yield palavra
        
texto = "Esta é uma frase de exemplo"

generator = pega_palavras(texto)

for palavra in generator:
    print(palavra)