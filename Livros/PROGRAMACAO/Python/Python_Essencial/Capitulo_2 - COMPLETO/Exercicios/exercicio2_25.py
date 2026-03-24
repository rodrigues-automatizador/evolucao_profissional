# Crie um programa que peça ao usuário para inserir 2 números,
# A e B e realizar uma operação com esses valores

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
operacao = input("Digite a operação: ")

operacao = operacao.upper()

match operacao:
    case "ADICAO":
        print(f"A soma dos valores é {a + b}")
        
    case "SUBTRACAO":
        print(f"A subtração dos valores é: {a - b}")
        
    case "MULTIPLICACAO":
        print(f"A multiplicação dos valores é: {a * b}")
        
    case "DIVISAO":
        print(f"A divisão dos valores é: {a / b}")
        
    case _:
        print("Operação e cálculos inválidos!")