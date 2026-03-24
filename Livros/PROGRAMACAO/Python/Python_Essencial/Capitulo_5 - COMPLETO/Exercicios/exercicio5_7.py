# Escreva uma função recursiva chamada contagemRegressiva que aceite um numero inteiro como entrada
# e imprima todos os números de n até zero seguidos por contagem regressiva finalizada! Por exemplo, 
# a chamada contagem regressiva(5) deve imprimir 5,4,3,2,1,0 contagem finalizada.

# Versão 1
def contagem_regressiva(numero):
    for i in range(numero + 1):
        print(numero - i)
    print("Contagem regresiva finalizada!")
    
contagem_regressiva(5)


# Versão correta!
def contagem_regressiva2(numero):
    if numero >= 0: 
        print(numero)
        contagem_regressiva2(numero - 1) 
    else:
        print("Contagem regressiva finalizada!")
        
contagem_regressiva2(5)