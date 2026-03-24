# Exemplo 1
# Criando funções

def saudacao(nome):
    print(f"Olá, {nome}!")
    
saudacao("Éder Rodrigues")
saudacao("Tânia Mara")


# Exemplo 2
# Argumentos posicionais

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)

# Exemplo 3
# Argumentos nomeados

def saudacao(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}")
    
saudacao(sobrenome="Rodrigues", nome="Souza")


# Exemplo 4
# Parâmetros opcionais

def potencia(base, expoente=2):
    return base ** expoente

resultado = potencia(3)
print(resultado)

resultado = potencia(3, 3)
print(resultado)


# Exemplo 5
# Argumentos combinados.

def calcular_imc(peso, altura, unidade='kg/m2'):
    if unidade == "kg/m2":
        return peso / altura ** 2
    
    elif unidade == "lb/in2":
        return 703 * peso / altura ** 2
    else:
        return None
    
resultado1 = calcular_imc(70, 1.75)
resultado2 = calcular_imc(154, 69, unidade="lb/in2")

print(resultado1)
print(resultado2)


# Exemplo 6
# Retorno de valores em funções

def soma(a, b):
    resultado = a + b
    return resultado

print(soma(2, 3))


# Exemplo 7
# Função de múltiplos retornos

def maior_e_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    
    return maior, menor

resultado = maior_e_menor([3,1,5,2])
print(resultado)


# Exemplo 8
# Trabalhando com retornos múltiplos

def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    
    return soma, subtracao, multiplicacao, divisao

adicao, subtracao, _, _ = operacoes(6, 2)
print(adicao, subtracao)


# Exemplo 9
# Parametros e retornos tipificados

def cumprimentar(nome: str) -> str:
    return "Olá, " + nome + "!"

print(cumprimentar("Rodrigues"))


# Exemplo 10
# Escopo de variáveis em funções

def soma(a, b):
    resultado10 = a + b
    return resultado10

print(soma(2, 3))
#print(resultado10)


# Exemplo 11
# Variável global

valor = 0
def somar(a, b):
    global valor
    valor = a + b
    
somar(2, 3)
print(valor)    