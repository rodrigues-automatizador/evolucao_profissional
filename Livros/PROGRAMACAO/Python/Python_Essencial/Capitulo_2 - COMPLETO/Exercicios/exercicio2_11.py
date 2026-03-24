# Crie um programa que verifique se uma pessoa pode votar ou não,
# considerando sua idade e nacionalidade, digitada pelo usuário
# ( se tem 16 anos ou mais e é brasileiro, pode votar).

idade = int(input("Digite a idade do eleitor: "))
nacionalidade = input("Digite a nacionalidade do eleitor: ")

nacionalidade = nacionalidade.upper()

if idade >= 16 and nacionalidade == "BRASILEIRO":
    print("Eleitor pode votar!")
    
else:
    print("Eleitor não pode votar!")