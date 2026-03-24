# Crie um programa que peça ao usuário para digitar um CPF
# Use a expressão regular para verificar se o CPF está no formato DDD.DDD.DDD-DD

while True:
    cpf = input("Digite um CPF com formáto válido: ")
    
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        print("CPF formato válido!")
        print(cpf)
        break
    else:
        print("CPF formato inválido! Digite novamente!")
