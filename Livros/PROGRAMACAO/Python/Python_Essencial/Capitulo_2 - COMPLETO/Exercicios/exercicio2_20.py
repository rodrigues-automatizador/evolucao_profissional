# Crie um programa que peça ao usuário para digitar um número de CPF
# e verifique se ele é válido. Considere que, para um CPF ser válido,
# ele deve ter exatamente 11 dígitos inteiro(use a função len())


cpf = input("Digite o CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido!")
    
else:
    print("CPF inválido!")