# Crie um generator que receba uma lista de números e retorne, a cada iteração, 
# o quadrado do próximo número da lista. Use esse generator para imprimir os 
# quadrados dos números de uma lista de 1 a 10

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def quadrados(lista):
    for numero in lista:
        yield numero ** 2
        
generator = quadrados(lista_numeros)
for quadrado in generator:
    print(quadrado)