# Exemplo 1
# utilizando função MAP

def dobro(x):
    return x * 2

numeros = [1,2,3,4,5]

resultado = list(map(dobro, numeros))
print(resultado)


# Exemplo 2
# função de ordem superior mais genérica

def aplicar_operacao(operacao, sequencia):
    resultado = []
    for elemento in sequencia:
        resultado.append(operacao(elemento))
        
    return resultado
    
def dobro(x):
    return x * 2

numeros = [1,2,3,4,5]
resultado = aplicar_operacao(dobro, numeros)
print(resultado)


# Exemplo Éder
def funcao_somatoria(numero):
    return numero + 2

potencia = lambda x: x ** 2
divisao = lambda x: x / 2
subtracao = lambda x: x - 2

lista_numero = [1,2,3,4,5]

resultado = list(map(funcao_somatoria, lista_numero))
print(resultado)

resultado = list(map(potencia, lista_numero))
print(resultado)