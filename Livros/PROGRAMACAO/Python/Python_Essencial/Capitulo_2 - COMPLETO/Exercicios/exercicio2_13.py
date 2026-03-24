# Crie um programa que verifique se um número inteiro digitado pelo usuário
# é divisível por outro inteiro também digitado pelo usuário

valor1 = int(input("Digite um número inteiro: "))
valor2 = int(input("Digite outro número inteiro: "))

if valor1 % valor2 == 0:
    print("Valor divisível!")
    
else:
    print("Valor não divisível!")
