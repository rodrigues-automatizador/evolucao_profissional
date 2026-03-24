# crie uma função que tenha um número inteiro como
# parâmetro e retorne True se o número for par e False se for ímpar

def par_impar(numero: int) -> int:
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = par_impar(10)
print(resultado)    